# -*- coding: utf-8 -*-
"""
Lösungs-Beispiel: gleiche fünf Elemente, diesmal barrierefrei umgesetzt.
"""
import wx
from ._common import (
    make_h1, make_h2, make_hint, ChartPanel,
    BFW_RED, BFW_RED_DARK, make_readonly_textctrl,
)


class LoesungenPage(wx.ScrolledWindow):
    def __init__(self, parent):
        super().__init__(parent, style=wx.VSCROLL | wx.TAB_TRAVERSAL)
        self.SetScrollRate(0, 20)
        self.SetBackgroundColour(wx.WHITE)
        self.SetName("Lösungs-Beispiel")

        s = wx.BoxSizer(wx.VERTICAL)
        s.Add(make_h1(self, "Lösungs-Beispiel (Python / wxPython)"), 0, wx.BOTTOM, 6)
        s.Add(
            wx.StaticText(
                self, label="Identische Beispiele – diesmal barrierefrei umgesetzt."
            ),
            0,
            wx.BOTTOM,
            12,
        )

        # --- 1: Beschriftetes Eingabefeld ---------------------------------
        s.Add(make_h2(self, "1. Beschriftetes Eingabefeld"), 0, wx.TOP, 8)
        lbl_name = wx.StaticText(self, label="&Vor- und Nachname")
        s.Add(lbl_name, 0, wx.TOP, 4)
        txt_name = wx.TextCtrl(self, size=(280, -1))
        txt_name.SetName("Vor- und Nachname")
        s.Add(txt_name, 0, wx.TOP, 2)
        s.Add(
            make_hint(self, "Lösung: StaticText mit Mnemonic + TextCtrl.SetName()."),
            0,
            wx.TOP,
            2,
        )

        # --- 2: Schreibgeschütztes Feld, aber tabbar ----------------------
        s.Add(make_h2(self, "2. Schreibgeschütztes, fokussierbares Feld"), 0, wx.TOP, 16)
        lbl_kdnr = wx.StaticText(self, label="&Kundennummer")
        s.Add(lbl_kdnr, 0, wx.TOP, 4)
        # WICHTIG: wxTextCtrl::AcceptsFocusFromKeyboard() liefert für
        # single-line read-only-Felder grundsätzlich False – das Feld
        # fliegt damit aus der Tab-Reihenfolge. Workaround: multiline +
        # TE_NO_VSCROLL + TE_DONTWRAP mit Höhe einer Zeile (siehe
        # make_readonly_textctrl). Optisch unverändert, technisch
        # multiline → bleibt tabbar.
        txt_kdnr = make_readonly_textctrl(self, value="K-4711", width=280)
        txt_kdnr.SetName("Kundennummer")
        s.Add(txt_kdnr, 0, wx.TOP, 2)
        s.Add(
            make_hint(
                self,
                "Lösung: read-only TextCtrl als Multiline (eine Zeile hoch) – "
                "bleibt fokussierbar.",
            ),
            0,
            wx.TOP,
            2,
        )

        # --- 3: Beschriftetes Diagramm ------------------------------------
        s.Add(make_h2(self, "3. Beschriftetes Diagramm"), 0, wx.TOP, 16)
        chart = ChartPanel(self, greyscale=False)
        # wx.Accessible setzt Rolle "Grafik" + Name + Beschreibung.
        chart.SetAccessibilityInfo(
            "Umsätze Q1 bis Q5",
            "Balkendiagramm: Q1 30, Q2 50, Q3 60, Q4 40, Q5 45 Tausend Euro.",
        )
        chart.SetToolTip(
            "Balkendiagramm: Q1 30, Q2 50, Q3 60, Q4 40, Q5 45 Tausend Euro."
        )
        s.Add(chart, 0, wx.TOP, 4)
        s.Add(
            make_hint(self, "Lösung: wx.Accessible mit Rolle Grafik + Name + Beschreibung."),
            0,
            wx.TOP,
            2,
        )

        # --- 4: Kontrast-konforme Schaltfläche ----------------------------
        s.Add(make_h2(self, "4. Schaltfläche mit ausreichendem Kontrast"), 0, wx.TOP, 16)
        btn = wx.Button(self, label="&Speichern")
        btn.SetForegroundColour(wx.WHITE)
        btn.SetBackgroundColour(BFW_RED)
        s.Add(btn, 0, wx.TOP, 4)
        s.Add(
            make_hint(self, "Lösung: WCAG-AA-konformes Kontrastverhältnis (weiß auf BFW-Rot)."),
            0,
            wx.TOP,
            2,
        )

        # --- 5: Icon-Schaltfläche mit Beschriftung -------------------------
        s.Add(make_h2(self, "5. Icon-Schaltfläche mit Beschriftung"), 0, wx.TOP, 16)
        bmp = wx.ArtProvider.GetBitmap(wx.ART_DELETE, wx.ART_BUTTON, (24, 24))
        icon_btn = wx.BitmapButton(self, bitmap=bmp)
        # WICHTIG: bei wx.BitmapButton liest NVDA/JAWS den Win32-Window-
        # Text als zugänglichen Namen, NICHT SetName(). Deshalb hier
        # zusätzlich SetLabel() – damit erscheint der Name am UIA-Knoten
        # des Controls.
        icon_btn.SetLabel("Eintrag löschen")
        icon_btn.SetName("Eintrag löschen")
        icon_btn.SetToolTip("Eintrag löschen")
        s.Add(icon_btn, 0, wx.TOP, 4)
        s.Add(
            make_hint(self, "Lösung: SetLabel() (für UIA-Name) + SetToolTip()."),
            0,
            wx.TOP | wx.BOTTOM,
            6,
        )

        # Linter-Hilfe: BFW_RED_DARK wird in dieser Datei nicht direkt
        # verwendet, aber aus Konsistenz mit den anderen Pages importiert.
        _ = BFW_RED_DARK

        self.SetSizer(s)
        self.Layout()
