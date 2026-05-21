# -*- coding: utf-8 -*-
import wx
from ._common import make_h1, make_h2, BFW_GREY_LIGHT


class HomePage(wx.ScrolledWindow):
    def __init__(self, parent):
        super().__init__(parent, style=wx.VSCROLL | wx.TAB_TRAVERSAL)
        self.SetScrollRate(0, 20)
        self.SetBackgroundColour(wx.WHITE)
        self.SetName("Startseite")

        s = wx.BoxSizer(wx.VERTICAL)
        s.Add(make_h1(self, "Barrierefreiheit – Python-Beispiel"), 0, wx.BOTTOM, 8)

        intro = wx.StaticText(
            self,
            label=(
                "Diese wxPython-Anwendung zeigt typische digitale Barrieren in einer\n"
                "klassischen Windows-Desktop-App – und stellt die gleichen Beispiele\n"
                "in der Variante „barrierefrei umgesetzt“ gegenüber."
            ),
        )
        s.Add(intro, 0, wx.BOTTOM, 12)

        hint = wx.StaticText(
            self,
            label=(
                "Wechseln Sie über das Menü zwischen Barrieren-Beispiel und Lösungs-\n"
                "Beispiel, um den Unterschied direkt mit NVDA oder JAWS zu erleben."
            ),
        )
        s.Add(hint, 0, wx.BOTTOM, 16)

        # Info-Karte
        card = wx.Panel(self)
        card.SetBackgroundColour(wx.Colour(0xF5, 0xF6, 0xF8))
        cs = wx.BoxSizer(wx.VERTICAL)
        cs.Add(make_h2(card, "Warum wxPython?"), 0, wx.ALL, 12)
        cs.Add(
            wx.StaticText(
                card,
                label=(
                    "wxPython verwendet unter Windows echte native Win32-Controls.\n"
                    "Damit liest NVDA und JAWS Name, Rolle und Wert jedes Steuer-\n"
                    "elements zuverlässig – ohne zusätzliche Bridges oder Tricks."
                ),
            ),
            0,
            wx.LEFT | wx.RIGHT | wx.BOTTOM,
            12,
        )
        card.SetSizer(cs)
        s.Add(card, 0, wx.EXPAND)

        self.SetSizer(s)
        self.Layout()
