# Barrierefreiheit.PythonGui

Python / wxPython 4.2+.

## Warum wxPython?

wxPython verwendet unter Windows **echte native Win32-Controls**. Dadurch
funktionieren MSAA und UI Automation ohne zusätzliche Bridges – NVDA und JAWS
lesen `wx.TextCtrl`, `wx.Button`, `wx.ListCtrl` & Co. zuverlässig vor und
melden Rolle, Name und Wert korrekt.

Tkinter ist bei Custom-Layouts noch immer holprig (Listboxen, Treeviews,
Notebook-Tabs werden teils unzureichend angekündigt). PySide6/Qt ist die
zweitbeste Wahl, kapselt aber Controls eigen-implementiert – weniger
nativ als wxPython.

## Voraussetzungen

* Python 3.11 oder 3.12 (3.13 sobald wxPython-Wheels verfügbar sind)
* `pip install -r requirements.txt`

## Start

```cmd
cd D:\Entwicklung\KI\Barrierefreiheit\Entwicklung\src\Barrierefreiheit.PythonGui
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Tastatur-Navigation

* `Tab` / `Shift+Tab` durch die Steuerelemente eines Bereichs
* `F6` / `Shift+F6` wechselt zwischen Menübereich und Inhalt (Windows-
  Konvention für „Pane-Wechsel", aus Outlook/Word/Visual Studio bekannt)
* `Alt+S` Startseite, `Alt+B` Barrieren, `Alt+L` Lösungen, `Alt+R` Über
* `Enter` / `Leertaste` aktiviert die fokussierte Schaltfläche

## Wichtige Stellen für Barrierefreiheit

* `pages/loesungen.py` – `SetName()`, `SetHelpText()`, `wx.TE_READONLY`,
  StaticText-Mnemonics (`&Vor- und Nachname`).
* `pages/_common.py` – `ChartPanel` mit `AcceptsFocusFromKeyboard()`.

## Hinweis zu Screenreader-Tests

* NVDA + JAWS gegentesten – beide nutzen MSAA/UIA leicht unterschiedlich.
* Speech Viewer (NVDA) bzw. Speech History (JAWS) am Beamer einblenden.
