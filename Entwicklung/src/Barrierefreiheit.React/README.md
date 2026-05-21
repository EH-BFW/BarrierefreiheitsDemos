# Barrierefreiheit.React

React 18 + TypeScript + Bootstrap 5 + React Router.

## Voraussetzungen

* Node.js 20 LTS oder neuer (`node --version`)
* npm 10+ (kommt mit Node)

## Start

```cmd
cd D:\Entwicklung\KI\Barrierefreiheit\Entwicklung\src\Barrierefreiheit.React
npm install
npm run dev
```

Öffnet automatisch `http://localhost:5173/`.

## Build (statisch)

```cmd
npm run build
npm run preview
```

`dist/` enthält danach statisches HTML/JS/CSS und kann auf jedem Webserver
ausgeliefert werden.

## Bedeutsame Stellen

* `src/App.tsx` – `FocusOnNavigate` setzt nach jedem Routenwechsel den Fokus auf
  `<main>`, damit Screenreader die neue Seite ankündigen.
* `src/pages/Loesungen.tsx` – `htmlFor`, `readOnly`, `role="img"`,
  `aria-labelledby`/`aria-describedby`, `aria-label`.
* `src/styles/bfw.css` – BFW-CD-Variablen, sichtbarer Fokus.
