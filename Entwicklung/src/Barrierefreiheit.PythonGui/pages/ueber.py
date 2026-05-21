# -*- coding: utf-8 -*-
import wx
from ._common import make_h1, make_h2, make_hint, BFW_ANTHRACITE


class UeberPage(wx.ScrolledWindow):
    def __init__(self, parent):
        super().__init__(parent, style=wx.VSCROLL | wx.TAB_TRAVERSAL)
        self.SetScrollRate(0, 20)
        self.SetBackgroundColour(wx.WHITE)
        self.SetName("Über diese App")

        s = wx.BoxSizer(wx.VERTICAL)
        s.Add(make_h1(self, "Über diese App"), 0, wx.BOTTOM, 8)

        s.Add(
            wx.StaticText(
                self,
                label=(
                    "Diese wxPython-Anwendung ist Teil der BFW-Würzburg-Veranstaltung\n"
                    "„Gemeinsam mehr Barrierefreiheit erreichen“. Sie zeigt typische\n"
                    "Barrieren in einer klassischen Windows-Desktop-App und gegenüber\n"
                    "die jeweilige barrierefreie Lösung."
                ),
            ),
            0,
            wx.BOTTOM,
            16,
        )

        s.Add(make_h2(self, "Entscheidende Stellen der Lösungs-Implementierung"), 0, wx.BOTTOM, 8)

        # Platzhalter 1
        ph1 = wx.TextCtrl(
            self,
            value=(
                'lbl = wx.StaticText(self, label="&Vor- und Nachname")\n'
                'txt = wx.TextCtrl(self, size=(280, -1))\n'
                'txt.SetName("Vor- und Nachname")'
            ),
            size=(700, 90),
            style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_DONTWRAP,
        )
        ph1.SetForegroundColour(wx.Colour(0x9B, 0xD8, 0x9C))
        ph1.SetBackgroundColour(BFW_ANTHRACITE)
        ph1.SetFont(
            wx.Font(
                10,
                wx.FONTFAMILY_TELETYPE,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                faceName="Consolas",
            )
        )
        s.Add(ph1, 0, wx.BOTTOM, 6)
        s.Add(
            make_hint(self, "Platzhalter 1 – bitte durch Screenshot ersetzen."),
            0,
            wx.BOTTOM,
            12,
        )

        # Platzhalter 2
        ph2 = wx.TextCtrl(
            self,
            value=(
                "chart.SetName(\"Umsätze Q1 bis Q5\")\n"
                "chart.SetHelpText(\"Balkendiagramm: ...\")\n"
                "chart.SetToolTip(\"Balkendiagramm: ...\")"
            ),
            size=(700, 90),
            style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_DONTWRAP,
        )
        ph2.SetForegroundColour(wx.Colour(0x9B, 0xD8, 0x9C))
        ph2.SetBackgroundColour(BFW_ANTHRACITE)
        ph2.SetFont(
            wx.Font(
                10,
                wx.FONTFAMILY_TELETYPE,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                faceName="Consolas",
            )
        )
        s.Add(ph2, 0, wx.BOTTOM, 6)
        s.Add(
            make_hint(self, "Platzhalter 2 – bitte durch Screenshot ersetzen."),
            0,
            wx.BOTTOM,
            12,
        )

        self.SetSizer(s)
        self.Layout()
