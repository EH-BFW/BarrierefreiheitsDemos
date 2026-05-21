# BFW Würzburg – Beispielprojekte „Anwendungen barrierefrei entwickeln"

Diese Solution begleitet die Veranstaltung **„Gemeinsam mehr Barrierefreiheit
erreichen"** und zeigt in vier Mini-Apps typische digitale Barrieren – und ihre
barrierefreie Umsetzung – in den vier wichtigsten C#-UI-Stacks von .NET.

## Projekte

| Projekt | Stack | Plattform |
|---|---|---|
| `Barrierefreiheit.Web` | Blazor Server (ASP.NET Core) | Browser |
| `Barrierefreiheit.Wpf` | WPF | Windows |
| `Barrierefreiheit.WinUI` | WinUI 3 (Windows App SDK) | Windows 10/11 |
| `Barrierefreiheit.Maui` | .NET MAUI | Windows · Android · iOS · Mac Catalyst |
| `Barrierefreiheit.React` | React 18 + TypeScript + Bootstrap 5 | Browser (statisch) |
| `Barrierefreiheit.PythonGui` | Python + wxPython (native Win32) | Windows |

Jedes Projekt enthält genau dieselben vier Menüpunkte:

1. **Startseite** – Kurzbeschreibung mit Bild
2. **Barrieren-Beispiel** – fünf typische Hürden für Screenreader
3. **Lösungs-Beispiel** – exakt dieselben fünf Elemente, barrierefrei umgesetzt
4. **Über (diese App)** – Sinn der App + Platzhalter für Screenshots der Lösung

Die fünf Beispiele sind in allen vier Apps inhaltlich identisch:

1. Unbeschriftetes Eingabefeld
2. Tastatur-nicht-fokussierbares Eingabefeld (`disabled` statt `readonly` /
   `IsEnabled=False` statt `IsReadOnly=True`)
3. Fokussierbares, aber unbeschriftetes Diagramm
4. Schaltfläche mit zu schwachem Kontrast
5. Icon-Schaltfläche ohne Beschriftung

## Voraussetzungen

* **.NET 9 SDK** (`dotnet --version` → 9.0.x)
* **Visual Studio 2022** 17.12 oder neuer (oder JetBrains Rider 2024.3+)
* Für **WinUI 3**: Workload *„Windows App SDK C# Templates"* + Windows 10/11
* Für **MAUI**: Workload `maui` (`dotnet workload install maui`)
  * Android: Android-SDK-Workload
  * iOS / Mac Catalyst: Build nur auf macOS möglich (oder remote via Pair to Mac)

```cmd
dotnet workload install maui
dotnet restore D:\Entwicklung\KI\Barrierefreiheit\Entwicklung\Barrierefreiheit.sln
```

## Starten

In Visual Studio: Projekt als Startprojekt setzen → F5.

Per Kommandozeile:

```cmd
:: Web
dotnet run --project src\Barrierefreiheit.Web

:: WPF
dotnet run --project src\Barrierefreiheit.Wpf

:: WinUI 3 (unpackaged)
dotnet run --project src\Barrierefreiheit.WinUI

:: MAUI – Windows
dotnet build src\Barrierefreiheit.Maui -t:Run -f net9.0-windows10.0.19041.0

:: MAUI – Android (Emulator/Gerät verbunden)
dotnet build src\Barrierefreiheit.Maui -t:Run -f net9.0-android
```

### React + Bootstrap

```cmd
cd src\Barrierefreiheit.React
npm install
npm run dev
```

Startet auf `http://localhost:5173/`. Details in
`src\Barrierefreiheit.React\README.md`.

### Python (wxPython)

```cmd
cd src\Barrierefreiheit.PythonGui
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Details und Begründung der Bibliotheks­wahl in
`src\Barrierefreiheit.PythonGui\README.md`.

## Hinweise zur Screenreader-Demo

* **NVDA**: Starten → Tab-Taste in jedem Beispiel; im Lösungs-Beispiel
  hört man Name + ggf. Beschreibung. Im Barrieren-Beispiel bleibt der
  Vorlese-Text leer oder unbrauchbar.
* **JAWS**: Analog. Bei der WPF/WinUI-App über die UI-Automation-Brücke.
* **NVDA Speech-Viewer** (NVDA-Menü → Werkzeuge) ist während der
  Präsentation sehr hilfreich, um Beamer-Publikum mitlesen zu lassen.

## Corporate Design

Die Apps verwenden die BFW-Würzburg-Farben:

| Rolle | Hex |
|---|---|
| Primär (Akzent) | `#C8102E` |
| Primär dunkel | `#9C0C24` |
| Anthrazit (Header) | `#1F2A36` |
| Grau (Sekundärtext) | `#5A6470` |
| Hellgrau (Trennlinien) | `#E9ECEF` |

Die Werte sind je App als Ressourcen zentralisiert (`App.xaml` bzw.
`wwwroot\app.css`) und lassen sich an die aktuell verbindlichen
CD-Werte anpassen.

## Über-Seite: Screenshots

Die „Über"-Seiten enthalten **Platzhaltergrafiken**. Bitte ersetzen Sie
diese durch eigene Screenshots der entscheidenden Code- oder
Programm-Stellen:

* `src\Barrierefreiheit.Web\wwwroot\images\about-web-1.svg`, `about-web-2.svg`
* Für WPF/WinUI/MAUI: Platzhalter sind XAML-Codeblöcke direkt auf der
  „Über"-Seite – einfach durch `<Image Source="…"/>` mit eigenem
  Screenshot austauschen.
