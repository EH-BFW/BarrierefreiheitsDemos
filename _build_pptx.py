# -*- coding: utf-8 -*-
"""
Erstellt die Präsentation
'Anwendungen prüfen, anpassen und barrierefrei entwickeln'
im Corporate Design des BFW Würzburg.
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree

# ---------- CD ----------
RED = RGBColor(0xC8, 0x10, 0x2E)
RED_DARK = RGBColor(0x9C, 0x0C, 0x24)
ANTHRACITE = RGBColor(0x1F, 0x2A, 0x36)
GREY = RGBColor(0x5A, 0x64, 0x70)
GREY_LIGHT = RGBColor(0xE9, 0xEC, 0xEF)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
NEAR_WHITE = RGBColor(0xF5, 0xF6, 0xF8)
CODE_BG = RGBColor(0x1F, 0x2A, 0x36)
CODE_FG = RGBColor(0x9B, 0xD8, 0x9C)

HEAD_FONT = "Calibri"
BODY_FONT = "Calibri"

# ---------- Setup ----------
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height

BLANK = prs.slide_layouts[6]


def add_rect(slide, x, y, w, h, fill, line=None):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = Pt(0.75)
    shp.shadow.inherit = False
    return shp


def add_triangle(slide, x, y, w, h, fill):
    shp = slide.shapes.add_shape(MSO_SHAPE.RIGHT_TRIANGLE, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    shp.line.fill.background()
    shp.rotation = -90  # Spitze nach rechts
    return shp


def add_text(slide, x, y, w, h, text, *,
             size=18, bold=False, italic=False, color=ANTHRACITE,
             font=BODY_FONT, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
             line_spacing=1.15):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Emu(0)
    tf.margin_right = Emu(0)
    tf.margin_top = Emu(0)
    tf.margin_bottom = Emu(0)
    tf.vertical_anchor = anchor
    lines = text.split("\n") if isinstance(text, str) else text
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        r = p.add_run()
        r.text = line
        r.font.name = font
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = color
    return tb


def add_bullets(slide, x, y, w, h, items, *,
                size=16, color=ANTHRACITE, font=BODY_FONT, indent=0):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Emu(0); tf.margin_right = Emu(0)
    tf.margin_top = Emu(0); tf.margin_bottom = Emu(0)
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.line_spacing = 1.2
        p.space_after = Pt(4)
        # Bullet als '•' via Text-Präfix (robust ohne XML-Bullet-Hack)
        r1 = p.add_run()
        r1.text = "•  "
        r1.font.name = font; r1.font.size = Pt(size); r1.font.color.rgb = RED; r1.font.bold = True
        r2 = p.add_run()
        r2.text = item
        r2.font.name = font; r2.font.size = Pt(size); r2.font.color.rgb = color
    return tb


def add_corner_brand(slide, dark=True):
    """Dezenter Marken-Akzent oben links."""
    if dark:
        bg = ANTHRACITE; fg_text = WHITE
    else:
        bg = NEAR_WHITE; fg_text = ANTHRACITE
    # Akzent-Dreieck
    tri = slide.shapes.add_shape(MSO_SHAPE.RIGHT_TRIANGLE, Inches(0.5), Inches(0.42), Inches(0.22), Inches(0.22))
    tri.fill.solid(); tri.fill.fore_color.rgb = RED
    tri.line.fill.background()
    tri.rotation = -90
    add_text(slide, Inches(0.85), Inches(0.36), Inches(8), Inches(0.4),
             "BFW Würzburg  ·  Barrierefreiheit",
             size=11, bold=True, color=fg_text)


def add_page_footer(slide, page_num, total, section=""):
    add_rect(slide, Emu(0), SH - Inches(0.35), SW, Inches(0.35), NEAR_WHITE)
    if section:
        add_text(slide, Inches(0.5), SH - Inches(0.33), Inches(10), Inches(0.3),
                 section, size=9, color=GREY, italic=True)
    add_text(slide, SW - Inches(1.5), SH - Inches(0.33), Inches(1.0), Inches(0.3),
             f"{page_num} / {total}", size=9, color=GREY, align=PP_ALIGN.RIGHT)


# ----------------------------------------------------------------
# Slide 1: Titel
# ----------------------------------------------------------------
def slide_title():
    s = prs.slides.add_slide(BLANK)
    # Vollflächiger Anthrazit-Hintergrund
    add_rect(s, 0, 0, SW, SH, ANTHRACITE)
    # Roter Block links (Akzent)
    add_rect(s, 0, 0, Inches(0.45), SH, RED)
    # Großes Dreieck-Logo
    tri = s.shapes.add_shape(MSO_SHAPE.RIGHT_TRIANGLE, Inches(0.95), Inches(0.7), Inches(0.55), Inches(0.55))
    tri.fill.solid(); tri.fill.fore_color.rgb = RED; tri.line.fill.background(); tri.rotation = -90

    add_text(s, Inches(1.65), Inches(0.75), Inches(10), Inches(0.5),
             "BFW Würzburg gGmbH", size=14, bold=True, color=WHITE)

    add_text(s, Inches(0.95), Inches(2.0), Inches(11.5), Inches(2.3),
             ["Anwendungen prüfen,", "anpassen und barrierefrei", "entwickeln"],
             size=54, bold=True, color=WHITE, line_spacing=1.05)

    # Roter Trennstrich
    add_rect(s, Inches(0.95), Inches(5.0), Inches(1.2), Pt(4), RED)

    add_text(s, Inches(0.95), Inches(5.15), Inches(12), Inches(0.6),
             "Veranstaltung „Gemeinsam mehr Barrierefreiheit erreichen“",
             size=22, color=GREY_LIGHT)

    add_text(s, Inches(0.95), Inches(5.85), Inches(12), Inches(0.4),
             "Ernst Heßdörfer  ·  IT-Teamleitung, BFW Würzburg",
             size=14, color=GREY_LIGHT)
    add_text(s, Inches(0.95), Inches(6.30), Inches(12), Inches(0.4),
             "Mai 2026",
             size=12, italic=True, color=RGBColor(0xBB,0xBB,0xBB))


# ----------------------------------------------------------------
# Slide 2: Agenda
# ----------------------------------------------------------------
def slide_agenda():
    s = prs.slides.add_slide(BLANK)
    add_corner_brand(s, dark=False)
    add_text(s, Inches(0.5), Inches(0.95), Inches(12), Inches(0.8),
             "Agenda", size=36, bold=True, color=RED)
    # Untertitel
    add_text(s, Inches(0.5), Inches(1.7), Inches(12), Inches(0.4),
             "Drei Bausteine eines barrierefreien Software-Lebenszyklus",
             size=16, italic=True, color=GREY)

    # 3 Karten
    cards = [
        ("1", "Prüfen", "Anwendungen systematisch auf Barrierefreiheit testen – mit Screenreader, Tastatur und Tools.", "≈ 2 Min."),
        ("2", "Anpassen", "Screenreader (NVDA, JAWS) so einrichten, dass typische Probleme zuverlässig auffallen.", "≈ 2–3 Min."),
        ("3", "Entwickeln", "Barrierefrei programmieren – mit Beispielen für Web, WPF, WinUI und MAUI.", "≈ 10 Min."),
    ]
    card_w = Inches(4.0); card_h = Inches(4.2); gap = Inches(0.27)
    total = card_w*3 + gap*2
    x0 = Inches(0.5)
    y0 = Inches(2.55)
    for i, (num, title, body, time) in enumerate(cards):
        x = x0 + (card_w + gap) * i
        # Karten-Hintergrund
        add_rect(s, x, y0, card_w, card_h, NEAR_WHITE, line=GREY_LIGHT)
        # roter Balken oben
        add_rect(s, x, y0, card_w, Inches(0.12), RED)
        # Zahl
        add_text(s, x + Inches(0.3), y0 + Inches(0.35), Inches(1.5), Inches(1.2),
                 num, size=72, bold=True, color=RED, line_spacing=1.0)
        # Titel
        add_text(s, x + Inches(0.3), y0 + Inches(1.6), card_w - Inches(0.6), Inches(0.6),
                 title, size=24, bold=True, color=ANTHRACITE)
        # Body
        add_text(s, x + Inches(0.3), y0 + Inches(2.25), card_w - Inches(0.6), Inches(1.7),
                 body, size=14, color=ANTHRACITE)
        # Zeit
        add_text(s, x + Inches(0.3), y0 + card_h - Inches(0.55), card_w - Inches(0.6), Inches(0.4),
                 time, size=12, italic=True, color=GREY)


# ----------------------------------------------------------------
# Section header generator
# ----------------------------------------------------------------
def slide_section(num, title, subtitle):
    s = prs.slides.add_slide(BLANK)
    add_rect(s, 0, 0, SW, SH, ANTHRACITE)
    add_rect(s, 0, 0, Inches(0.35), SH, RED)
    add_text(s, Inches(0.95), Inches(1.6), Inches(2), Inches(1.8),
             num, size=180, bold=True, color=RED, line_spacing=1.0)
    add_text(s, Inches(3.4), Inches(2.2), Inches(9.5), Inches(1.2),
             title, size=54, bold=True, color=WHITE)
    add_text(s, Inches(3.4), Inches(3.6), Inches(9.5), Inches(1.2),
             subtitle, size=20, italic=True, color=GREY_LIGHT)
    add_rect(s, Inches(3.4), Inches(4.6), Inches(1.0), Pt(4), RED)


# ----------------------------------------------------------------
# Slide: Testen #1 – Warum & was
# ----------------------------------------------------------------
def slide_pruefen_warum():
    s = prs.slides.add_slide(BLANK)
    add_corner_brand(s, dark=False)
    add_text(s, Inches(0.5), Inches(0.9), Inches(12), Inches(0.7),
             "Anwendungen prüfen – Warum und was?",
             size=30, bold=True, color=RED)
    # Roter Strich
    add_rect(s, Inches(0.5), Inches(1.55), Inches(0.8), Pt(3), RED)

    # Linke Spalte
    add_text(s, Inches(0.5), Inches(1.85), Inches(6), Inches(0.5),
             "Warum prüfen?", size=20, bold=True, color=ANTHRACITE)
    add_bullets(s, Inches(0.5), Inches(2.45), Inches(6), Inches(4),
                ["BFSG, EU-Web­barriere­freiheits­richtlinie, BITV 2.0 verlangen Nachweise.",
                 "Blinde Mitarbeitende stoßen sonst täglich auf Hürden – Praktika scheitern.",
                 "Frühe Funde sind 10–100× billiger als Nachbesserungen im Betrieb.",
                 "Barrierefreiheit erhöht generelle Bedienbarkeit (Stichwort „Curb-Cut-Effekt“)."],
                size=14)

    # Rechte Spalte – POUR-Karten
    add_text(s, Inches(7.0), Inches(1.85), Inches(6), Inches(0.5),
             "Was prüfen? – WCAG-Prinzipien (POUR)", size=20, bold=True, color=ANTHRACITE)
    pour = [
        ("P", "Perceivable", "Wahrnehmbar – Textalternativen, Kontrast, Struktur."),
        ("O", "Operable", "Bedienbar – Tastatur, Fokus, ausreichend Zeit."),
        ("U", "Understandable", "Verständlich – klare Sprache, Fehler­meldungen, Hilfen."),
        ("R", "Robust", "Robust – semantisches Markup, ARIA, UI Automation."),
    ]
    y = Inches(2.45)
    for letter, head, body in pour:
        # Kreisförmige Marke
        circ = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(7.0), y, Inches(0.6), Inches(0.6))
        circ.fill.solid(); circ.fill.fore_color.rgb = RED; circ.line.fill.background()
        tf = circ.text_frame
        tf.margin_left = Emu(0); tf.margin_right = Emu(0); tf.margin_top = Emu(0); tf.margin_bottom = Emu(0)
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = letter
        r.font.bold = True; r.font.color.rgb = WHITE; r.font.size = Pt(18); r.font.name = HEAD_FONT
        add_text(s, Inches(7.75), y - Inches(0.05), Inches(5.5), Inches(0.4),
                 head, size=14, bold=True, color=ANTHRACITE)
        add_text(s, Inches(7.75), y + Inches(0.3), Inches(5.5), Inches(0.6),
                 body, size=12, color=GREY)
        y = y + Inches(0.95)


# ----------------------------------------------------------------
# Slide: Testen #2 – Wie / Werkzeuge
# ----------------------------------------------------------------
def slide_pruefen_wie():
    s = prs.slides.add_slide(BLANK)
    add_corner_brand(s, dark=False)
    add_text(s, Inches(0.5), Inches(0.9), Inches(12), Inches(0.7),
             "Wie prüfen? – Drei sich ergänzende Ebenen",
             size=30, bold=True, color=RED)
    add_rect(s, Inches(0.5), Inches(1.55), Inches(0.8), Pt(3), RED)

    cards = [
        ("Mit Tastatur",
         "Maus weg!",
         ["Tab / Shift+Tab durch alles bedienen.",
          "Fokus immer sichtbar? Logische Reihenfolge?",
          "Keine Tastatur­fallen (Modale, Custom-Controls).",
          "Enter / Space / Escape funktionieren?"]),
        ("Mit Screenreader",
         "NVDA + JAWS",
         ["Vorlesen jedes interaktiven Elements: Name, Rolle, Wert.",
          "Browse-/Fokus-Modus (Web) bzw. Objekt­navigation testen.",
          "Live-Regions, Statusmeldungen, Fehlerausgaben.",
          "Demo-Tipp: NVDA Speech-Viewer für den Beamer."]),
        ("Mit Tools",
         "Schnellprüfung & Reports",
         ["Browser: axe DevTools, WAVE, Lighthouse.",
          "Kontraste: Colour Contrast Analyser (CCA).",
          "Windows-Apps: Accessibility Insights for Windows.",
          "PDFs: PAC 2024 / Adobe Pro Vollprüfung."]),
    ]
    cw = Inches(4.0); ch = Inches(5.0); gap = Inches(0.27)
    x0 = Inches(0.5); y0 = Inches(1.9)
    for i, (head, sub, items) in enumerate(cards):
        x = x0 + (cw + gap) * i
        add_rect(s, x, y0, cw, ch, NEAR_WHITE, line=GREY_LIGHT)
        add_rect(s, x, y0, cw, Inches(0.12), RED)
        add_text(s, x + Inches(0.3), y0 + Inches(0.3), cw - Inches(0.6), Inches(0.5),
                 head, size=20, bold=True, color=ANTHRACITE)
        add_text(s, x + Inches(0.3), y0 + Inches(0.85), cw - Inches(0.6), Inches(0.4),
                 sub, size=13, italic=True, color=RED)
        add_bullets(s, x + Inches(0.3), y0 + Inches(1.35), cw - Inches(0.6), Inches(3.5),
                    items, size=12)


# ----------------------------------------------------------------
# Slide: NVDA Anpassungen
# ----------------------------------------------------------------
def slide_nvda():
    s = prs.slides.add_slide(BLANK)
    add_corner_brand(s, dark=False)
    add_text(s, Inches(0.5), Inches(0.9), Inches(12), Inches(0.7),
             "Screenreader-Anpassungen · NVDA",
             size=30, bold=True, color=RED)
    add_rect(s, Inches(0.5), Inches(1.55), Inches(0.8), Pt(3), RED)
    add_text(s, Inches(0.5), Inches(1.7), Inches(12), Inches(0.4),
             "Open-Source-Screenreader, ideal für die Demo und für Entwickler-Tests.",
             size=14, italic=True, color=GREY)

    # Linke Spalte: Einstellungen
    add_text(s, Inches(0.5), Inches(2.3), Inches(6), Inches(0.5),
             "Wichtige Einstellungen", size=18, bold=True, color=ANTHRACITE)
    add_bullets(s, Inches(0.5), Inches(2.85), Inches(6), Inches(4),
                ["Stimme: eSpeak-NG für klare Demo; Sprech­geschwindigkeit ~25–30 %.",
                 "Tastatur-Layout: Desktop (NVDA = Einf) oder Laptop (NVDA = Caps).",
                 "Spracherkennung von Symbolen: „Manche“ (für Vorträge angenehmer).",
                 "Maus-Verfolgung aus, Fokus-Verfolgung an.",
                 "Modus „Strukturzeichen“ wechseln: NVDA+P (Punkte / Wörter / alle).",
                 "Add-ons: NVDA Remote, Tony's Add-Ons, Speech History."],
                size=13)

    # Rechte Spalte: Demo-Hilfen
    add_text(s, Inches(6.95), Inches(2.3), Inches(6), Inches(0.5),
             "Hilfen für die Demonstration", size=18, bold=True, color=ANTHRACITE)
    add_bullets(s, Inches(6.95), Inches(2.85), Inches(6), Inches(4),
                ["Speech Viewer (NVDA-Menü → Werkzeuge → Sprach­anzeige) – Publikum liest mit.",
                 "Eingabe-Hilfe (NVDA+1): zeigt jede Taste mit Funktion an.",
                 "Log-Viewer (NVDA+F1) für Debugging fehlerhafter ARIA-Bindings.",
                 "Browser-Modus mit NVDA+Leertaste umschalten.",
                 "Schnelle Navigation: H für Headings, F für Felder, B für Buttons.",
                 "Konfigurationsprofile pro Anwendung möglich."],
                size=13)


# ----------------------------------------------------------------
# Slide: JAWS
# ----------------------------------------------------------------
def slide_jaws():
    s = prs.slides.add_slide(BLANK)
    add_corner_brand(s, dark=False)
    add_text(s, Inches(0.5), Inches(0.9), Inches(12), Inches(0.7),
             "Screenreader-Anpassungen · JAWS",
             size=30, bold=True, color=RED)
    add_rect(s, Inches(0.5), Inches(1.55), Inches(0.8), Pt(3), RED)
    add_text(s, Inches(0.5), Inches(1.7), Inches(12), Inches(0.4),
             "Marktführer im professionellen Umfeld – im BFW Standard für Mitarbeitende.",
             size=14, italic=True, color=GREY)

    add_text(s, Inches(0.5), Inches(2.3), Inches(6), Inches(0.5),
             "Wichtige Einstellungen", size=18, bold=True, color=ANTHRACITE)
    add_bullets(s, Inches(0.5), Inches(2.85), Inches(6), Inches(4),
                ["Stimme: Vocalizer Expert (z.B. „Anna“) ~280–320 Worte/Min.",
                 "Tastatur-Layout: Desktop (JAWS-Key = Einf) oder Laptop (Caps).",
                 "Ausführlichkeit: „Mittel“; Symbole „Manche“.",
                 "Modus „Schneller Datei-Zugriff“ + Smart-Navigation an.",
                 "Tutor-Meldungen für die Demo abschalten (Insert + V).",
                 "Settings Center pro Anwendung anpassbar (z.B. Word, Outlook, Browser)."],
                size=13)

    add_text(s, Inches(6.95), Inches(2.3), Inches(6), Inches(0.5),
             "Spezialitäten", size=18, bold=True, color=ANTHRACITE)
    add_bullets(s, Inches(6.95), Inches(2.85), Inches(6), Inches(4),
                ["JAWS-Cursor / PC-Cursor / virtuelles Cursor-Modell (Insert + Z bzw. +).",
                 "JAWS Inspect (Freedom Scientific) für automatisierte Reports.",
                 "Skripting in JSS für firmenspezifische Anwendungen.",
                 "Picture Smart (KI-Bildbeschreibung) seit JAWS 2023.",
                 "Convenient OCR für Bild-Texte und gescannte PDFs.",
                 "Pro-Tipp: Mit NVDA gegentesten – beide nutzen MSAA/UIA unterschiedlich."],
                size=13)


# ----------------------------------------------------------------
# Slide: Take-aways Anpassungen (NVDA + JAWS gemeinsam)
# ----------------------------------------------------------------
def slide_nvda_jaws_tipps():
    s = prs.slides.add_slide(BLANK)
    add_corner_brand(s, dark=False)
    add_text(s, Inches(0.5), Inches(0.9), Inches(12), Inches(0.7),
             "NVDA & JAWS – Tipps für Entwicklung und Demo",
             size=30, bold=True, color=RED)
    add_rect(s, Inches(0.5), Inches(1.55), Inches(0.8), Pt(3), RED)

    # Drei Karten quer
    cards = [
        ("Beide gegentesten",
         "Auf MSAA, IA2 und UIA reagieren NVDA und JAWS unterschiedlich. Was bei einem leise bleibt, fällt beim anderen auf."),
        ("Vorlesegeschwindigkeit reduzieren",
         "Für die Demo 25–30 % langsamer als gewohnt – das Publikum braucht Sekunden, um den Vorlesetext zu erfassen."),
        ("Sprach­ausgabe sichtbar machen",
         "NVDA Speech Viewer bzw. JAWS Speech History (Insert+Pfeil hoch, dann Backslash) per Beamer."),
    ]
    cw = Inches(4.0); ch = Inches(4.5); gap = Inches(0.27)
    x0 = Inches(0.5); y0 = Inches(2.0)
    for i, (h, body) in enumerate(cards):
        x = x0 + (cw + gap) * i
        add_rect(s, x, y0, cw, ch, NEAR_WHITE, line=GREY_LIGHT)
        add_rect(s, x, y0, Inches(0.12), ch, RED)
        add_text(s, x + Inches(0.4), y0 + Inches(0.4), cw - Inches(0.7), Inches(1.0),
                 h, size=20, bold=True, color=ANTHRACITE)
        add_text(s, x + Inches(0.4), y0 + Inches(1.4), cw - Inches(0.7), Inches(3.0),
                 body, size=14, color=ANTHRACITE)


# ----------------------------------------------------------------
# Slide: Prinzipien
# ----------------------------------------------------------------
def slide_prinzipien():
    s = prs.slides.add_slide(BLANK)
    add_corner_brand(s, dark=False)
    add_text(s, Inches(0.5), Inches(0.9), Inches(12), Inches(0.7),
             "Barrierefrei entwickeln – Leitplanken",
             size=30, bold=True, color=RED)
    add_rect(s, Inches(0.5), Inches(1.55), Inches(0.8), Pt(3), RED)

    add_text(s, Inches(0.5), Inches(1.7), Inches(12), Inches(0.4),
             "Plattform­unabhängige Grundregeln, die sich auf Web, WPF, WinUI und MAUI gleichermaßen anwenden lassen.",
             size=14, italic=True, color=GREY)

    items = [
        ("Name, Rolle, Wert",
         "Jedes interaktive Element braucht einen zugänglichen Namen (was), eine Rolle (welche Art) und einen Wert (Zustand)."),
        ("Tastatur zuerst",
         "Tab-Reihenfolge logisch, Fokus immer sichtbar, keine Maus-only-Interaktionen. Disabled nur, wenn Inhalt wirklich nicht relevant ist."),
        ("Struktur und Semantik",
         "Überschriften-Hierarchien, Landmarks (header, main, nav), Tabellen mit echten Headern – nicht nur optisch nachbauen."),
        ("Kontrast und Größe",
         "WCAG 2.2 AA: 4,5:1 für Text, 3:1 für UI-Komponenten. Mindest-Klickfläche 24 × 24 CSS-Pixel."),
        ("Status­meldungen ansprechen",
         "Erfolgs- und Fehlermeldungen über Live-Regions / AutomationProperty.LiveSetting bekanntgeben."),
    ]
    # Zwei Spalten
    col_w = Inches(6.0)
    y = Inches(2.5)
    for i, (head, body) in enumerate(items):
        col = i % 2
        row = i // 2
        x = Inches(0.5) + (col_w + Inches(0.4)) * col
        yy = y + Inches(1.45) * row
        # Index-Block
        idx = s.shapes.add_shape(MSO_SHAPE.OVAL, x, yy + Inches(0.05), Inches(0.45), Inches(0.45))
        idx.fill.solid(); idx.fill.fore_color.rgb = RED; idx.line.fill.background()
        tf = idx.text_frame
        tf.margin_left = Emu(0); tf.margin_right = Emu(0); tf.margin_top = Emu(0); tf.margin_bottom = Emu(0)
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = str(i + 1)
        r.font.bold = True; r.font.color.rgb = WHITE; r.font.size = Pt(16); r.font.name = HEAD_FONT
        add_text(s, x + Inches(0.6), yy, col_w - Inches(0.6), Inches(0.45),
                 head, size=16, bold=True, color=ANTHRACITE)
        add_text(s, x + Inches(0.6), yy + Inches(0.45), col_w - Inches(0.6), Inches(0.9),
                 body, size=12, color=GREY)


# ----------------------------------------------------------------
# Slide: APIs Tabelle
# ----------------------------------------------------------------
def slide_apis():
    s = prs.slides.add_slide(BLANK)
    add_corner_brand(s, dark=False)
    add_text(s, Inches(0.5), Inches(0.9), Inches(12), Inches(0.7),
             "Plattformen & Barrierefreiheits-APIs",
             size=30, bold=True, color=RED)
    add_rect(s, Inches(0.5), Inches(1.55), Inches(0.8), Pt(3), RED)

    cols = ["Stack", "API-Schicht", "Wichtigste Konstrukte"]
    rows = [
        ("Web (Blazor / Razor)", "ARIA + WAI-ARIA",
         "<label for>, role=\"…\", aria-label, aria-labelledby, aria-describedby, semantische HTML-Elemente"),
        ("WPF", "MSAA + UI Automation",
         "AutomationProperties.Name / .HelpText / .LabeledBy, Label-Target + AccessText, IsReadOnly statt IsEnabled"),
        ("WinUI 3", "UI Automation",
         "AutomationProperties.* (analog WPF), TextBox.Header, ToolTipService.ToolTip, NavigationView-Semantik"),
        (".NET MAUI", "Plattform-Brücken zu UIA, AccessibilityNodeInfo, UIAccessibility",
         "SemanticProperties.Description / .Hint / .HeadingLevel, SemanticScreenReader.Announce"),
    ]
    table_x = Inches(0.5); table_y = Inches(2.1)
    widths = [Inches(2.5), Inches(3.0), Inches(7.0)]
    row_h = [Inches(0.55)] + [Inches(0.95)] * len(rows)

    # Kopfzeile
    x = table_x
    for i, c in enumerate(cols):
        add_rect(s, x, table_y, widths[i], row_h[0], ANTHRACITE)
        add_text(s, x + Inches(0.15), table_y + Inches(0.12), widths[i] - Inches(0.3), row_h[0] - Inches(0.15),
                 c, size=14, bold=True, color=WHITE)
        x += widths[i]

    # Daten
    yy = table_y + row_h[0]
    for ri, row in enumerate(rows):
        x = table_x
        bg = WHITE if ri % 2 == 0 else NEAR_WHITE
        for i, cell in enumerate(row):
            add_rect(s, x, yy, widths[i], row_h[ri + 1], bg, line=GREY_LIGHT)
            add_text(s, x + Inches(0.15), yy + Inches(0.12), widths[i] - Inches(0.3), row_h[ri + 1] - Inches(0.15),
                     cell, size=12, color=ANTHRACITE)
            x += widths[i]
        yy += row_h[ri + 1]

    add_text(s, Inches(0.5), Inches(6.7), Inches(12), Inches(0.4),
             "Gemeinsamer Nenner: jede Plattform bietet einen Mechanismus, einem Control Name, Rolle und Wert zuzuweisen.",
             size=12, italic=True, color=GREY)


# ----------------------------------------------------------------
# Slide: 5 typische Barrieren (Tabelle)
# ----------------------------------------------------------------
def slide_barrieren_tabelle():
    s = prs.slides.add_slide(BLANK)
    add_corner_brand(s, dark=False)
    add_text(s, Inches(0.5), Inches(0.9), Inches(12), Inches(0.7),
             "Fünf typische Barrieren – und ihre Lösung",
             size=30, bold=True, color=RED)
    add_rect(s, Inches(0.5), Inches(1.55), Inches(0.8), Pt(3), RED)
    add_text(s, Inches(0.5), Inches(1.7), Inches(12), Inches(0.4),
             "Diese fünf Fälle sind in allen vier Beispiel-Apps (Web, WPF, WinUI, MAUI) identisch umgesetzt.",
             size=14, italic=True, color=GREY)

    cols = ["#", "Barriere", "Lösung"]
    rows = [
        ("1", "Eingabefeld ohne Beschriftung",
         "label/aria-label/Header bzw. AutomationProperties.LabeledBy oder SemanticProperties.Description"),
        ("2", "Feld disabled / IsEnabled=False statt readonly",
         "readonly / IsReadOnly=true – Fokus und Vorlesbarkeit bleiben erhalten."),
        ("3", "Diagramm fokussierbar, aber ohne Namen",
         "role=img + aria-labelledby/-describedby bzw. AutomationProperties.Name + HelpText"),
        ("4", "Schaltfläche mit zu schwachem Kontrast",
         "WCAG-AA-Kontrast ≥ 4,5:1 (Text) bzw. ≥ 3:1 (Komponenten) sicherstellen."),
        ("5", "Icon-Schaltfläche ohne Beschriftung",
         "aria-label / AutomationProperties.Name / SemanticProperties.Description + Tooltip"),
    ]
    table_x = Inches(0.5); table_y = Inches(2.15)
    widths = [Inches(0.5), Inches(5.0), Inches(7.0)]
    h_head = Inches(0.5); h_row = Inches(0.85)
    x = table_x
    for i, c in enumerate(cols):
        add_rect(s, x, table_y, widths[i], h_head, ANTHRACITE)
        add_text(s, x + Inches(0.15), table_y + Inches(0.10), widths[i] - Inches(0.2), h_head - Inches(0.12),
                 c, size=14, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER if i == 0 else PP_ALIGN.LEFT)
        x += widths[i]

    yy = table_y + h_head
    for ri, row in enumerate(rows):
        x = table_x
        bg = WHITE if ri % 2 == 0 else NEAR_WHITE
        for i, cell in enumerate(row):
            add_rect(s, x, yy, widths[i], h_row, bg, line=GREY_LIGHT)
            add_text(s, x + Inches(0.15), yy + Inches(0.18), widths[i] - Inches(0.2), h_row - Inches(0.18),
                     cell, size=13,
                     bold=(i == 0),
                     color=RED if i == 0 else ANTHRACITE,
                     align=PP_ALIGN.CENTER if i == 0 else PP_ALIGN.LEFT)
            x += widths[i]
        yy += h_row


# ----------------------------------------------------------------
# Code-Slide Helper
# ----------------------------------------------------------------
def slide_codeexample(stack, subtitle, bad_caption, bad_code, good_caption, good_code):
    s = prs.slides.add_slide(BLANK)
    add_corner_brand(s, dark=False)
    add_text(s, Inches(0.5), Inches(0.9), Inches(12), Inches(0.7),
             f"Beispiel · {stack}", size=30, bold=True, color=RED)
    add_rect(s, Inches(0.5), Inches(1.55), Inches(0.8), Pt(3), RED)
    add_text(s, Inches(0.5), Inches(1.7), Inches(12), Inches(0.4),
             subtitle, size=14, italic=True, color=GREY)

    col_w = Inches(6.0); gap = Inches(0.3); col_h = Inches(4.7)
    x_left = Inches(0.5); x_right = x_left + col_w + gap
    y0 = Inches(2.3)

    # BAD
    add_text(s, x_left, y0, col_w, Inches(0.4), "Barriere", size=16, bold=True, color=RED)
    add_text(s, x_left, y0 + Inches(0.4), col_w, Inches(0.4), bad_caption, size=11, italic=True, color=GREY)
    add_rect(s, x_left, y0 + Inches(0.85), col_w, col_h - Inches(0.85), CODE_BG)
    add_text(s, x_left + Inches(0.2), y0 + Inches(1.0), col_w - Inches(0.4), col_h - Inches(1.05),
             bad_code, size=11, color=CODE_FG, font="Consolas", line_spacing=1.2)

    # GOOD
    add_text(s, x_right, y0, col_w, Inches(0.4), "Lösung", size=16, bold=True, color=RGBColor(0x2E,0x7D,0x32))
    add_text(s, x_right, y0 + Inches(0.4), col_w, Inches(0.4), good_caption, size=11, italic=True, color=GREY)
    add_rect(s, x_right, y0 + Inches(0.85), col_w, col_h - Inches(0.85), CODE_BG)
    add_text(s, x_right + Inches(0.2), y0 + Inches(1.0), col_w - Inches(0.4), col_h - Inches(1.05),
             good_code, size=11, color=CODE_FG, font="Consolas", line_spacing=1.2)


def slide_web():
    bad = (
        "<input type=\"text\" />\n"
        "\n"
        "<input type=\"text\" value=\"K-4711\" disabled />\n"
        "\n"
        "<div class=\"chart\" tabindex=\"0\">\n"
        "  <svg>…Balken…</svg>\n"
        "</div>\n"
        "\n"
        "<button style=\"color:#CCC\">Speichern</button>\n"
        "\n"
        "<button><svg>…Müll-Icon…</svg></button>"
    )
    good = (
        "<label for=\"name\">Vor- und Nachname\n"
        "  <input id=\"name\" type=\"text\" />\n"
        "</label>\n"
        "\n"
        "<input value=\"K-4711\" readonly />\n"
        "\n"
        "<div role=\"img\" tabindex=\"0\"\n"
        "     aria-labelledby=\"t\" aria-describedby=\"d\">…</div>\n"
        "\n"
        "<button class=\"primary\">Speichern</button>\n"
        "\n"
        "<button aria-label=\"Eintrag löschen\">…</button>"
    )
    slide_codeexample(
        "Web (Blazor Server / Razor)",
        "Standard-HTML mit ARIA – funktioniert in jedem Browser mit jedem Screenreader.",
        "Unbeschriftet, disabled, ohne Rolle/Name, kontrastarm, ohne Label.",
        bad,
        "Label/for, readonly, role=\"img\" + aria-*, ausreichender Kontrast, aria-label.",
        good)


def slide_wpf():
    bad = (
        "<TextBox />\n"
        "\n"
        "<TextBox Text=\"K-4711\" IsEnabled=\"False\" />\n"
        "\n"
        "<Border Focusable=\"True\">\n"
        "  <!-- Balken-Canvas -->\n"
        "</Border>\n"
        "\n"
        "<Button Foreground=\"#CCC\" Background=\"White\"\n"
        "        Content=\"Speichern\" />\n"
        "\n"
        "<Button><Path … /></Button>"
    )
    good = (
        "<Label x:Name=\"LblName\" Target=\"{Binding\n"
        "  ElementName=TxtName}\">\n"
        "  <AccessText Text=\"_Vor- und Nachname\" />\n"
        "</Label>\n"
        "<TextBox x:Name=\"TxtName\"\n"
        "  AutomationProperties.LabeledBy=\"{Binding\n"
        "    ElementName=LblName}\" />\n"
        "\n"
        "<TextBox Text=\"K-4711\" IsReadOnly=\"True\" />\n"
        "\n"
        "<Border Focusable=\"True\"\n"
        "  AutomationProperties.Name=\"Umsätze Q1-Q5\"\n"
        "  AutomationProperties.HelpText=\"Q1 30, …\" />"
    )
    slide_codeexample(
        "WPF (.NET 9, net9.0-windows)",
        "Klassische Desktop-Apps – über UI Automation an NVDA/JAWS angebunden.",
        "Unbeschriftete TextBox, IsEnabled=False entzieht den Fokus, kein Name.",
        bad,
        "Label.Target + AccessText, AutomationProperties.LabeledBy, IsReadOnly.",
        good)


def slide_winui():
    bad = (
        "<TextBox />\n"
        "\n"
        "<TextBox Text=\"K-4711\" IsEnabled=\"False\" />\n"
        "\n"
        "<Border IsTabStop=\"True\">\n"
        "  <!-- Diagramm -->\n"
        "</Border>\n"
        "\n"
        "<Button Foreground=\"#CCC\"\n"
        "        Content=\"Speichern\" />\n"
        "\n"
        "<Button><SymbolIcon Symbol=\"Delete\"/></Button>"
    )
    good = (
        "<TextBox Header=\"Vor- und Nachname\"\n"
        "  AutomationProperties.LabeledBy=\"{Binding\n"
        "    ElementName=LblName}\" />\n"
        "\n"
        "<TextBox Header=\"Kundennummer\"\n"
        "         Text=\"K-4711\" IsReadOnly=\"True\" />\n"
        "\n"
        "<Border IsTabStop=\"True\"\n"
        "  AutomationProperties.Name=\"Umsätze Q1-Q5\"\n"
        "  AutomationProperties.HelpText=\"Q1 30, …\" />\n"
        "\n"
        "<Button AutomationProperties.Name=\"Eintrag löschen\"\n"
        "  ToolTipService.ToolTip=\"Eintrag löschen\">\n"
        "  <SymbolIcon Symbol=\"Delete\"/>\n"
        "</Button>"
    )
    slide_codeexample(
        "WinUI 3 (Windows App SDK 1.6)",
        "Modernes Windows-UI – APIs analog zu WPF, etwas knapper.",
        "TextBox ohne Header, IsEnabled=False, IconButton ohne Namen.",
        bad,
        "TextBox.Header, AutomationProperties.LabeledBy / .Name / .HelpText.",
        good)


def slide_maui():
    bad = (
        "<Entry />\n"
        "\n"
        "<Entry Text=\"K-4711\" IsEnabled=\"False\" />\n"
        "\n"
        "<Frame>\n"
        "  <GraphicsView … />\n"
        "</Frame>\n"
        "\n"
        "<Button Text=\"Speichern\"\n"
        "        TextColor=\"#CCC\"\n"
        "        BackgroundColor=\"White\" />\n"
        "\n"
        "<Button Text=\"🗑\" />"
    )
    good = (
        "<Entry SemanticProperties.Description=\n"
        "         \"Vor- und Nachname\"\n"
        "       SemanticProperties.Hint=\"Pflichtfeld\" />\n"
        "\n"
        "<Entry Text=\"K-4711\" IsReadOnly=\"True\" />\n"
        "\n"
        "<Frame SemanticProperties.Description=\n"
        "         \"Umsätze Q1 bis Q5\"\n"
        "       SemanticProperties.Hint=\"Q1 30, …\" />\n"
        "\n"
        "<Button Style=\"{StaticResource PrimaryButton}\"\n"
        "        Text=\"Speichern\" />\n"
        "\n"
        "<Button Text=\"🗑\"\n"
        "  SemanticProperties.Description=\"Eintrag löschen\" />"
    )
    slide_codeexample(
        ".NET MAUI (Windows · Android · iOS · Mac Catalyst)",
        "Eine Codebasis, vier Plattformen – Semantic-Properties werden plattformgerecht übersetzt.",
        "Entry / Frame ohne semantische Annotation, IsEnabled statt IsReadOnly.",
        bad,
        "SemanticProperties.Description + .Hint, IsReadOnly, klare Button-Namen.",
        good)


# ----------------------------------------------------------------
# Take-aways + Kontakt
# ----------------------------------------------------------------
def slide_takeaways():
    s = prs.slides.add_slide(BLANK)
    add_rect(s, 0, 0, SW, SH, ANTHRACITE)
    add_rect(s, 0, 0, Inches(0.35), SH, RED)
    add_text(s, Inches(0.95), Inches(0.7), Inches(12), Inches(1.0),
             "Take-aways", size=44, bold=True, color=WHITE)
    add_rect(s, Inches(0.95), Inches(1.75), Inches(1.0), Pt(4), RED)

    items = [
        ("Testen",      "Tastatur, Screenreader und ein Tool – diese drei Linsen finden 90 % der Probleme."),
        ("Anpassen",    "NVDA und JAWS gegentesten, Speech-Viewer einschalten – Publikum darf mitlesen."),
        ("Entwickeln",  "Name, Rolle, Wert für jedes Control. readonly statt disabled. Kontrast ≥ 4,5:1."),
        ("Wirken",      "Barrierefreie Software ist Voraussetzung für berufliche Teilhabe – nicht Kür."),
    ]
    y = Inches(2.2)
    for i, (h, b) in enumerate(items):
        # Punkt-Kreis
        circ = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.95), y + Inches(0.1), Inches(0.55), Inches(0.55))
        circ.fill.solid(); circ.fill.fore_color.rgb = RED; circ.line.fill.background()
        tf = circ.text_frame
        tf.margin_left = Emu(0); tf.margin_right = Emu(0); tf.margin_top = Emu(0); tf.margin_bottom = Emu(0)
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = str(i + 1)
        r.font.bold = True; r.font.color.rgb = WHITE; r.font.size = Pt(20); r.font.name = HEAD_FONT
        add_text(s, Inches(1.7), y, Inches(11), Inches(0.5),
                 h, size=20, bold=True, color=WHITE)
        add_text(s, Inches(1.7), y + Inches(0.45), Inches(11), Inches(0.6),
                 b, size=14, color=GREY_LIGHT)
        y = y + Inches(0.95)

    add_rect(s, Inches(0.95), Inches(6.45), Inches(11.4), Pt(2), RED)
    add_text(s, Inches(0.95), Inches(6.55), Inches(11), Inches(0.4),
             "Ernst Heßdörfer · IT-Teamleitung · it.leitung@bfw-wuerzburg.de",
             size=14, color=GREY_LIGHT)
    add_text(s, Inches(0.95), Inches(6.95), Inches(11), Inches(0.4),
             "BFW Würzburg gGmbH · Bildungszentrum für Blinde und Sehbehinderte · www.bfw-wuerzburg.de",
             size=11, italic=True, color=RGBColor(0xBB,0xBB,0xBB))


# ---------- Build ----------
slides_builders = [
    slide_title,
    slide_agenda,
    lambda: slide_section("1", "Prüfen", "Anwendungen systematisch auf Barrierefreiheit testen"),
    slide_pruefen_warum,
    slide_pruefen_wie,
    lambda: slide_section("2", "Anpassen", "Screenreader (NVDA & JAWS) demo- und entwicklungsfreundlich einrichten"),
    slide_nvda,
    slide_jaws,
    slide_nvda_jaws_tipps,
    lambda: slide_section("3", "Entwickeln", "Barrierefreie Anwendungen in Web, WPF, WinUI und MAUI"),
    slide_prinzipien,
    slide_apis,
    slide_barrieren_tabelle,
    slide_web,
    slide_wpf,
    slide_winui,
    slide_maui,
    slide_takeaways,
]

for b in slides_builders:
    b()

# Footer / Foliennummer auf nicht-Titel-/Sektionsfolien
total = len(prs.slides)
SECTION_INDICES = {0, 2, 5, 9, 17}  # 0-basiert: Titel, 3 Sections, Take-aways
SECTION_TEXT = {
    1: "Agenda",
    3: "1 · Prüfen", 4: "1 · Prüfen",
    6: "2 · Anpassen", 7: "2 · Anpassen", 8: "2 · Anpassen",
    10: "3 · Entwickeln", 11: "3 · Entwickeln", 12: "3 · Entwickeln",
    13: "3 · Entwickeln", 14: "3 · Entwickeln", 15: "3 · Entwickeln", 16: "3 · Entwickeln",
}
for i, slide in enumerate(prs.slides):
    if i in SECTION_INDICES:
        continue
    add_page_footer(slide, i + 1, total, SECTION_TEXT.get(i, ""))

out = r"/sessions/pensive-gifted-wozniak/mnt/Barrierefreiheit/Praesentation_Barrierefreiheit.pptx"
prs.save(out)
print("OK", out, "slides:", len(prs.slides))
