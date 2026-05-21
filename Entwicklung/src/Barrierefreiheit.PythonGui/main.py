# -*- coding: utf-8 -*-
"""
BFW Würzburg – Barrierefreiheit (Python / wxPython)
====================================================

wxPython verwendet unter Windows echte native Win32-Controls, die von
NVDA und JAWS direkt über MSAA / UI Automation erfasst werden.
Damit ist wxPython auf Windows aktuell die zuverlässigste Wahl für
barrierefreie Python-GUIs.

Tastatur-Bedienung:
    Tab / Shift+Tab    durch alle interaktiven Elemente eines Bereichs
    F6 / Shift+F6      Bereich wechseln (Menü ↔ Inhalt)
    Alt+S              Startseite
    Alt+B              Barrieren-Beispiel
    Alt+L              Lösungs-Beispiel
    Alt+R              Über diese App
    Enter / Leertaste  aktiviert die fokussierte Schaltfläche

Start:
    python main.py
"""

import wx

from pages.home       import HomePage
from pages.barrieren  import BarrierenPage
from pages.loesungen  import LoesungenPage
from pages.ueber      import UeberPage


# BFW-CD
BFW_RED        = wx.Colour(0xC8, 0x10, 0x2E)
BFW_RED_DARK   = wx.Colour(0x9C, 0x0C, 0x24)
BFW_ANTHRACITE = wx.Colour(0x1F, 0x2A, 0x36)
BFW_GREY       = wx.Colour(0x5A, 0x64, 0x70)
BFW_GREY_LIGHT = wx.Colour(0xE9, 0xEC, 0xEF)
BFW_BG_LIGHT   = wx.Colour(0xF5, 0xF6, 0xF8)
WHITE          = wx.Colour(0xFF, 0xFF, 0xFF)


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(
            parent=None,
            title="BFW Würzburg – Barrierefreiheit (Python / wxPython)",
            size=(1000, 700),
        )
        self.SetBackgroundColour(WHITE)
        self._nav_buttons = []
        self._build_ui()
        self.show_page("home")
        self._setup_accelerators()
        # Initial-Fokus auf den ersten Nav-Button, damit Tab/Shift+Tab
        # sofort durch das Menü navigiert
        if self._nav_buttons:
            self._nav_buttons[0].SetFocus()
        self.Centre()

    # ------------------------------------------------------------------
    # UI-Aufbau
    # ------------------------------------------------------------------
    def _build_ui(self):
        outer = wx.BoxSizer(wx.VERTICAL)

        outer.Add(self._build_header(), 0, wx.EXPAND)
        outer.Add(self._build_nav(),    0, wx.EXPAND)

        # Inhaltsbereich = Panel mit austauschbarem Sizer
        self.content = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        self.content.SetBackgroundColour(WHITE)
        self.content.SetName("Inhaltsbereich")
        self.content_sizer = wx.BoxSizer(wx.VERTICAL)
        self.content.SetSizer(self.content_sizer)
        outer.Add(self.content, 1, wx.EXPAND)

        outer.Add(self._build_footer(), 0, wx.EXPAND)

        self.SetSizer(outer)

    def _build_header(self):
        hdr = wx.Panel(self)
        hdr.SetBackgroundColour(BFW_ANTHRACITE)
        s = wx.BoxSizer(wx.HORIZONTAL)
        s.AddSpacer(16)

        bmp = self._red_triangle_bitmap(20)
        s.Add(wx.StaticBitmap(hdr, bitmap=bmp), 0,
              wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM, 10)
        s.AddSpacer(10)

        lbl = wx.StaticText(hdr, label="BFW Würzburg · Barrierefreiheit (Python)")
        lbl.SetForegroundColour(WHITE)
        font = lbl.GetFont()
        font.SetWeight(wx.FONTWEIGHT_SEMIBOLD)
        font.SetPointSize(font.GetPointSize() + 1)
        lbl.SetFont(font)
        s.Add(lbl, 0, wx.ALIGN_CENTER_VERTICAL)
        hdr.SetSizer(s)
        return hdr

    def _build_nav(self):
        # Wrapper-Panel als Parent – enthält Button-Leiste + rote Trennlinie
        wrapper = wx.Panel(self, style=wx.TAB_TRAVERSAL)

        nav = wx.Panel(wrapper, style=wx.TAB_TRAVERSAL)
        nav.SetBackgroundColour(BFW_BG_LIGHT)
        s = wx.BoxSizer(wx.HORIZONTAL)
        s.AddSpacer(8)
        # Eindeutige Mnemonics: Alt+S / Alt+B / Alt+L / Alt+R
        buttons = [
            ("&Startseite",         "home"),
            ("&Barrieren-Beispiel", "barrieren"),
            ("&Lösungs-Beispiel",   "loesungen"),
            ("Übe&r diese App",     "ueber"),
        ]
        for label, key in buttons:
            btn = wx.Button(nav, label=label)
            btn.SetName(label.replace("&", ""))
            btn.Bind(wx.EVT_BUTTON, lambda _e, k=key: self.show_page(k))
            s.Add(btn, 0, wx.ALL, 6)
            self._nav_buttons.append(btn)
        nav.SetSizer(s)

        # Rote Trennlinie (3 px) unter der Button-Leiste
        line = wx.Panel(wrapper, size=(-1, 3))
        line.SetBackgroundColour(BFW_RED)

        wsz = wx.BoxSizer(wx.VERTICAL)
        wsz.Add(nav, 0, wx.EXPAND)
        wsz.Add(line, 0, wx.EXPAND)
        wrapper.SetSizer(wsz)
        return wrapper

    def _build_footer(self):
        f = wx.Panel(self)
        f.SetBackgroundColour(BFW_BG_LIGHT)
        s = wx.BoxSizer(wx.HORIZONTAL)
        s.AddSpacer(16)
        lbl = wx.StaticText(
            f,
            label=("© 2026 BFW Würzburg gGmbH – Beispiel-App zur digitalen "
                   "Barrierefreiheit (Python / wxPython)"),
        )
        lbl.SetForegroundColour(BFW_GREY)
        font = lbl.GetFont()
        font.SetPointSize(font.GetPointSize() - 1)
        lbl.SetFont(font)
        s.Add(lbl, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM, 8)
        f.SetSizer(s)
        return f

    # ------------------------------------------------------------------
    # Tastatur-Shortcuts
    # ------------------------------------------------------------------
    def _setup_accelerators(self):
        """Globale Tastenkürzel im Frame.

        * Alt+S / Alt+B / Alt+L / Alt+R aktivieren die Nav-Buttons
          (Mnemonics auf den Buttons funktionieren in wxPython nicht aus
          jedem Fokus-Kontext – AcceleratorTable greift überall).
        * F6 / Shift+F6 wechseln zwischen Menübereich und Inhaltsbereich –
          die Windows-Standardgeste für „Pane-Wechsel" (siehe Outlook,
          Word, Visual Studio).
        """
        entries = []

        # Alt+Buchstabe → Nav-Buttons
        keys = ["S", "B", "L", "R"]
        for i, k in enumerate(keys):
            if i >= len(self._nav_buttons):
                break
            cmd_id = wx.NewIdRef()
            btn = self._nav_buttons[i]
            entries.append(wx.AcceleratorEntry(wx.ACCEL_ALT, ord(k), int(cmd_id)))
            self.Bind(
                wx.EVT_MENU,
                lambda _e, b=btn: self._activate_button(b),
                id=int(cmd_id),
            )

        # F6 → nächster Bereich; Shift+F6 → vorheriger Bereich
        next_id = wx.NewIdRef()
        prev_id = wx.NewIdRef()
        entries.append(wx.AcceleratorEntry(wx.ACCEL_NORMAL, wx.WXK_F6, int(next_id)))
        entries.append(wx.AcceleratorEntry(wx.ACCEL_SHIFT,  wx.WXK_F6, int(prev_id)))
        self.Bind(wx.EVT_MENU, lambda _e: self._cycle_pane(forward=True),  id=int(next_id))
        self.Bind(wx.EVT_MENU, lambda _e: self._cycle_pane(forward=False), id=int(prev_id))

        self.SetAcceleratorTable(wx.AcceleratorTable(entries))

    def _activate_button(self, button: wx.Button):
        evt = wx.CommandEvent(wx.wxEVT_BUTTON, button.GetId())
        evt.SetEventObject(button)
        wx.PostEvent(button, evt)

    # ------------------------------------------------------------------
    # F6 / Shift+F6 – Bereich wechseln
    # ------------------------------------------------------------------
    def _cycle_pane(self, forward: bool):
        """Wechselt den Fokus zwischen Menübereich und Inhaltsbereich.

        Vorwärts (F6):   Menü → Inhalt → Menü → …
        Rückwärts (Shift+F6): Menü → Inhalt → Menü → … (gleicher Zyklus,
        da wir nur zwei Bereiche haben).
        """
        del forward  # bei nur zwei Bereichen identisch
        focused = wx.Window.FindFocus()
        in_content = self._is_descendant_of(focused, self.content)
        if in_content:
            # Zurück ins Menü
            if self._nav_buttons:
                self._nav_buttons[0].SetFocus()
        else:
            # Hinein in die aktuelle Page – erstes fokussierbares Element
            first = self._first_focusable(self.content)
            if first is not None:
                first.SetFocus()
            else:
                # Page hat (noch) keine fokussierbaren Elemente:
                # zumindest die Page selbst fokussieren
                pages = self.content.GetChildren()
                if pages:
                    pages[0].SetFocus()

    @staticmethod
    def _is_descendant_of(child: wx.Window, ancestor: wx.Window) -> bool:
        w = child
        while w is not None:
            if w is ancestor:
                return True
            w = w.GetParent()
        return False

    @classmethod
    def _first_focusable(cls, parent: wx.Window):
        """Sucht rekursiv das erste per Tastatur fokussierbare Kind-Window."""
        for child in parent.GetChildren():
            if child.IsShownOnScreen() and child.IsEnabled() \
                    and child.AcceptsFocusFromKeyboard():
                # StaticText etc. liefern hier False – wir bekommen
                # nur echte interaktive Controls.
                return child
            deeper = cls._first_focusable(child)
            if deeper is not None:
                return deeper
        return None

    # ------------------------------------------------------------------
    # Navigation
    # ------------------------------------------------------------------
    def show_page(self, key: str):
        page_cls_map = {
            "home":      HomePage,
            "barrieren": BarrierenPage,
            "loesungen": LoesungenPage,
            "ueber":     UeberPage,
        }
        # Alte Inhalte entfernen
        for child in list(self.content.GetChildren()):
            child.Destroy()
        self.content_sizer.Clear()

        cls = page_cls_map[key]
        page = cls(self.content)
        self.content_sizer.Add(page, 1, wx.EXPAND | wx.ALL, 16)
        self.content.Layout()
        # Bewusst KEIN page.SetFocus() – sonst würde jeder Klick auf einen
        # Nav-Button den Fokus aus dem Menü ziehen und die Tastatur-
        # Navigation per Tab/Shift+Tab durch die Menüleiste unterbrechen.

    # ------------------------------------------------------------------
    # Helper: kleines rotes Logo-Dreieck als Bitmap
    # ------------------------------------------------------------------
    def _red_triangle_bitmap(self, size: int) -> wx.Bitmap:
        bmp = wx.Bitmap(size, size, 32)
        bmp.UseAlpha()
        dc = wx.MemoryDC(bmp)
        gc = wx.GraphicsContext.Create(dc)
        gc.SetBrush(wx.Brush(BFW_RED))
        gc.SetPen(wx.TRANSPARENT_PEN)
        path = gc.CreatePath()
        path.MoveToPoint(0, 0)
        path.AddLineToPoint(size, size / 2)
        path.AddLineToPoint(0, size)
        path.CloseSubpath()
        gc.FillPath(path)
        del dc
        return bmp


class BfwApp(wx.App):
    def OnInit(self):
        self.SetUseBestVisual(True)
        frame = MainFrame()
        frame.Show()
        return True


if __name__ == "__main__":
    BfwApp().MainLoop()
