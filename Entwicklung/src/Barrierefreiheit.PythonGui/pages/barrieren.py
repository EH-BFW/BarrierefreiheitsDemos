# -*- coding: utf-8 -*-
"""
Barrieren-Beispiel: bewusst nicht barrierefrei.
"""
import wx
from ._common import make_h1, make_h2, ChartPanel


class BarrierenPage(wx.ScrolledWindow):
    def __init__(self, parent):
        super().__init__(parent, style=wx.VSCROLL | wx.TAB_TRAVERSAL)
        self.SetScrollRate(0, 20)
        self.SetBackgroundColour(wx.WHITE)
        self.SetName("Barrieren-Beispiel")

        s = wx.BoxSizer(wx.VERTICAL)
        s.Add(make_h1(self, "Barrieren-Beispiel (Python / wxPython)"), 0, wx.BOTTOM, 6)
        s.Add(
            wx.StaticText(self, label="Achtung: Diese Seite ist bewusst nicht barrierefrei."),
            0,
            wx.BOTTOM,
            12,
        )

        # --- 1: Unbeschriftetes Eingabefeld --------------------------------
        s.Add(make_h2(self, "1. Unbeschriftetes Eingabefeld"), 0, wx.TOP, 8)
        # BARRIERE: kein zugehöriges StaticText-Label, kein SetName/SetHelpText
        unlabeled = wx.TextCtrl(self, size=(280, -1))
        s.Add(unlabeled, 0, wx.TOP, 4)

        # --- 2: Disabled statt ReadOnly ------------------------------------
        s.Add(make_h2(self, "2. Per Tastatur nicht erreichbares Feld (Disabled)"), 0, wx.TOP, 16)
        s.Add(wx.StaticText(self, label="Kundennummer"), 0, wx.TOP, 4)
        kunden_disabled = wx.TextCtrl(self, value="K-4711", size=(280, -1))
        kunden_disabled.Disable()  # BARRIERE: Disable entzieht Fokus und Vorlesbarkeit
        s.Add(kunden_disabled, 0, wx.TOP, 2)

        # --- 3: Fokussierbares, unbeschriftetes Diagramm -------------------
        s.Add(make_h2(self, "3. Fokussierbares, aber unbeschriftetes Diagramm"), 0, wx.TOP, 16)
        chart_bad = ChartPanel(self, greyscale=True)
        # BARRIERE: kein SetName/SetHelpText
        s.Add(chart_bad, 0, wx.TOP, 4)

        # --- 4: Kontrastarme Schaltfläche ----------------------------------
        s.Add(make_h2(self, "4. Schaltfläche mit zu schwachem Kontrast"), 0, wx.TOP, 16)
        low_btn = wx.Button(self, label="Speichern")
        low_btn.SetForegroundColour(wx.Colour(0xCC, 0xCC, 0xCC))
        low_btn.SetBackgroundColour(wx.Colour(0xFF, 0xFF, 0xFF))
        s.Add(low_btn, 0, wx.TOP, 4)

        # --- 5: Icon-Schaltfläche ohne Beschriftung ------------------------
        s.Add(make_h2(self, "5. Icon-Schaltfläche ohne Beschriftung"), 0, wx.TOP, 16)
        # BARRIERE: BitmapButton ohne Label und ohne SetName
        bmp = wx.ArtProvider.GetBitmap(wx.ART_DELETE, wx.ART_BUTTON, (24, 24))
        icon_btn = wx.BitmapButton(self, bitmap=bmp)
        s.Add(icon_btn, 0, wx.TOP | wx.BOTTOM, 8)

        self.SetSizer(s)
        self.Layout()
