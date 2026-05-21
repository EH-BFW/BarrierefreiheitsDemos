# -*- coding: utf-8 -*-
"""
Gemeinsame Helfer für die Seiten: Überschriften, Hint-Labels, Farben
und ein eigenes ChartPanel mit korrekter MSAA/UIA-Anbindung.
"""
import wx

try:
    import ctypes
    _user32 = ctypes.windll.user32
except (ImportError, AttributeError, OSError):
    _user32 = None


def make_readonly_textctrl(parent: wx.Window, value: str, width: int = 280) -> wx.TextCtrl:
    """Erzeugt ein schreibgeschütztes TextCtrl, das tabbar bleibt.

    Warum nicht einfach ``SetEditable(False)`` / ``wx.TE_READONLY``?

    wxWidgets implementiert für ``wx.TextCtrl`` selbst:

        bool wxTextCtrl::AcceptsFocusFromKeyboard() const
        {
            return (IsEditable() || IsMultiLine())
                   && wxControl::AcceptsFocusFromKeyboard();
        }

    Ein **single-line, nicht editierbares** TextCtrl liefert hier
    ``false`` – damit fliegt es aus der Tab-Reihenfolge. Kein
    Win32-Style-Trick kann das überschreiben, weil wxPython die
    Methode vor der Tab-Navigation auswertet.

    Der zuverlässige Ausweg: das Control als **multiline** anlegen
    (mit deaktiviertem vertikalem Scrollbar und ohne Zeilenumbruch)
    und auf die Höhe einer Zeile beschränken. Optisch ein Single-Line-
    Feld, technisch multiline → bleibt tabbar und wird vom Screenreader
    als "schreibgeschütztes Textfeld" vorgelesen.
    """
    # Standard-Höhe eines Single-Line-Edits ermitteln (DPI-sicher)
    ref = wx.TextCtrl(parent)
    line_height = ref.GetBestSize().height
    ref.Destroy()

    style = (
        wx.TE_MULTILINE
        | wx.TE_READONLY
        | wx.TE_NO_VSCROLL
    )
    txt = wx.TextCtrl(parent, value=value, size=(width, line_height), style=style)
    return txt


def force_tabstop(window: wx.Window) -> None:
    """Erzwingt das ``WS_TABSTOP``-Flag auf einem Win32-Control.

    Hintergrund: ``wx.TextCtrl.SetEditable(False)`` bzw. ``wx.TE_READONLY``
    setzt unter Windows in vielen wxPython-Builds das ``WS_TABSTOP``-
    Bit des nativen Edit-Controls zurück. Das Feld ist dann aus der
    Tab-Reihenfolge gefallen. Wir setzen das Bit per Win32-API direkt
    wieder, damit das Control trotz Schreibschutz fokussierbar und
    vorlesbar bleibt.

    No-Op auf Nicht-Windows-Plattformen.
    """
    if _user32 is None or not hasattr(window, "GetHandle"):
        return
    GWL_STYLE  = -16
    WS_TABSTOP = 0x00010000
    try:
        hwnd = int(window.GetHandle())
        _user32.GetWindowLongW.restype  = ctypes.c_long
        _user32.GetWindowLongW.argtypes = [ctypes.c_void_p, ctypes.c_int]
        _user32.SetWindowLongW.restype  = ctypes.c_long
        _user32.SetWindowLongW.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_long]
        style = _user32.GetWindowLongW(hwnd, GWL_STYLE)
        _user32.SetWindowLongW(hwnd, GWL_STYLE, style | WS_TABSTOP)
    except Exception:
        # Best-Effort; bei Fehlern lieber ohne erzwungenes Tabstop weiter
        pass


BFW_RED        = wx.Colour(0xC8, 0x10, 0x2E)
BFW_RED_DARK   = wx.Colour(0x9C, 0x0C, 0x24)
BFW_ANTHRACITE = wx.Colour(0x1F, 0x2A, 0x36)
BFW_GREY       = wx.Colour(0x5A, 0x64, 0x70)
BFW_GREY_LIGHT = wx.Colour(0xE9, 0xEC, 0xEF)

# wx.Accessible ist Windows-only. Wir nutzen es, um eigene Controls
# (z.B. ChartPanel) gegenüber MSAA / UI Automation mit Rolle, Name und
# Beschreibung anzubinden.
HAS_ACCESSIBLE = hasattr(wx, "Accessible")


def make_h1(parent: wx.Window, text: str) -> wx.StaticText:
    h = wx.StaticText(parent, label=text)
    h.SetForegroundColour(BFW_RED)
    f = h.GetFont()
    f.SetPointSize(f.GetPointSize() + 8)
    f.SetWeight(wx.FONTWEIGHT_BOLD)
    h.SetFont(f)
    return h


def make_h2(parent: wx.Window, text: str) -> wx.StaticText:
    h = wx.StaticText(parent, label=text)
    h.SetForegroundColour(BFW_ANTHRACITE)
    f = h.GetFont()
    f.SetPointSize(f.GetPointSize() + 3)
    f.SetWeight(wx.FONTWEIGHT_BOLD)
    h.SetFont(f)
    return h


def make_hint(parent: wx.Window, text: str) -> wx.StaticText:
    h = wx.StaticText(parent, label=text)
    h.SetForegroundColour(BFW_GREY)
    f = h.GetFont()
    f.SetStyle(wx.FONTSTYLE_ITALIC)
    h.SetFont(f)
    return h


if HAS_ACCESSIBLE:

    class _ChartAccessible(wx.Accessible):
        """Verknüpft ein ChartPanel mit MSAA / UI Automation."""

        def __init__(self, window: wx.Window, name: str, description: str):
            super().__init__(window)
            self._name = name
            self._description = description

        def GetName(self, _childId):
            return (wx.ACC_OK, self._name)

        def GetDescription(self, _childId):
            return (wx.ACC_OK, self._description)

        def GetRole(self, _childId):
            # ROLE_SYSTEM_GRAPHIC = Bild / Grafik – Screenreader liest
            # das Element als "Grafik" statt als "Panel".
            return (wx.ACC_OK, wx.ROLE_SYSTEM_GRAPHIC)

        def GetState(self, _childId):
            state = wx.ACC_STATE_SYSTEM_FOCUSABLE
            win = self.GetWindow()
            if win is not None and win.HasFocus():
                state |= wx.ACC_STATE_SYSTEM_FOCUSED
            return (wx.ACC_OK, state)

        def GetChildCount(self):
            return (wx.ACC_OK, 0)


class ChartPanel(wx.Window):
    """
    Einfaches Balkendiagramm als eigener, tab-fokussierbarer Control.

    Wichtige Designentscheidungen für Barrierefreiheit:

    * Ableitung von ``wx.Window`` (nicht ``wx.Panel``):
      ``wx.Panel`` hat per Default ``wx.TAB_TRAVERSAL`` und ist damit
      ein Container, der Tab an seine Kinder weiterreicht – nicht selbst
      ein TabStop. ``wx.Window`` hat diesen Default nicht und kann mit
      ``AcceptsFocusFromKeyboard()`` zu einem regulären TabStop werden.
    * **Kein** ``wx.WANTS_CHARS``: dieser Style würde dem Control alle
      Tasten-Events zustellen – auch Tab – und damit den Fokus
      festhalten (klassische Tastaturfalle).
    * Eigene ``wx.Accessible``-Klasse: liefert Rolle "Grafik" sowie
      Name + Beschreibung an Screenreader.
    """

    VALUES = [30, 50, 60, 40, 45]

    def __init__(self, parent, greyscale: bool = False, size=(240, 100)):
        super().__init__(parent, size=size, style=wx.BORDER_SIMPLE)
        self.greyscale = greyscale
        self.SetBackgroundColour(wx.WHITE)
        self.Bind(wx.EVT_PAINT, self._on_paint)
        # Fokus-Rahmen neu zeichnen, wenn sich der Fokus ändert
        self.Bind(wx.EVT_SET_FOCUS,  lambda _e: self.Refresh())
        self.Bind(wx.EVT_KILL_FOCUS, lambda _e: self.Refresh())
        # Sicherheitsnetz: falls Tab doch hier landet, navigieren wir
        # selbst weiter zum nächsten/vorherigen TabStop.
        self.Bind(wx.EVT_KEY_DOWN, self._on_key_down)

    def AcceptsFocus(self):
        return True

    def AcceptsFocusFromKeyboard(self):
        return True

    def SetAccessibilityInfo(self, name: str, description: str):
        """Bindet Name + Beschreibung + Rolle (Grafik) an UI Automation."""
        self.SetName(name)           # Fallback
        self.SetHelpText(description)
        if HAS_ACCESSIBLE:
            self.SetAccessible(_ChartAccessible(self, name, description))

    def _on_key_down(self, evt: wx.KeyEvent):
        if evt.GetKeyCode() == wx.WXK_TAB:
            flags = wx.NavigationKeyEvent.IsForward
            if evt.ShiftDown():
                flags = 0  # rückwärts
            self.Navigate(flags)
            return
        evt.Skip()

    def _on_paint(self, _evt):
        dc = wx.PaintDC(self)
        dc.SetBackground(wx.Brush(wx.WHITE))
        dc.Clear()
        color = wx.Colour(0x88, 0x88, 0x88) if self.greyscale else BFW_RED
        dc.SetBrush(wx.Brush(color))
        dc.SetPen(wx.TRANSPARENT_PEN)
        base_x = 20
        for i, v in enumerate(self.VALUES):
            x = base_x + i * 30
            h = v
            y = 80 - h
            dc.DrawRectangle(x, y, 20, h)
        # Sichtbarer Fokusrahmen, wenn das Control den Fokus hat
        if self.HasFocus():
            w, hgt = self.GetClientSize()
            dc.SetBrush(wx.TRANSPARENT_BRUSH)
            dc.SetPen(wx.Pen(wx.Colour(0x00, 0x50, 0xB3), 2, wx.PENSTYLE_DOT))
            dc.DrawRectangle(1, 1, w - 2, hgt - 2)
