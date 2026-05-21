export default function Ueber() {
    return (
        <article>
            <h1 className="text-bfw-red">Über diese App</h1>
            <p>
                Dieses React-/Bootstrap-Beispiel ist Teil der BFW-Würzburg-Veranstaltung{" "}
                <em>„Gemeinsam mehr Barrierefreiheit erreichen"</em>. Es zeigt typische
                Barrieren im Web und – in identischer Optik – die jeweilige barrierefreie
                Lösung.
            </p>

            <h2 className="h5 mt-4">Entscheidende Stellen der Lösungs-Implementierung</h2>

            <figure className="my-3">
                <div
                    style={{
                        background: "#1F2A36",
                        color: "#9BD89C",
                        fontFamily: "Consolas, monospace",
                        padding: "1rem",
                        borderRadius: 4,
                        whiteSpace: "pre"
                    }}
                >
{`<label htmlFor="name">Vor- und Nachname</label>
<input id="name" type="text" autoComplete="name" />`}
                </div>
                <figcaption className="text-muted mt-1">
                    1. Explizite Verknüpfung von Label und Eingabefeld (Platzhalter – bitte durch Screenshot ersetzen).
                </figcaption>
            </figure>

            <figure className="my-3">
                <div
                    style={{
                        background: "#1F2A36",
                        color: "#9BD89C",
                        fontFamily: "Consolas, monospace",
                        padding: "1rem",
                        borderRadius: 4,
                        whiteSpace: "pre"
                    }}
                >
{`<div role="img" tabIndex={0}
     aria-labelledby="chart-title"
     aria-describedby="chart-desc">
  …SVG…
</div>`}
                </div>
                <figcaption className="text-muted mt-1">
                    2. Diagramm mit Textalternative für Screenreader (Platzhalter – bitte durch Screenshot ersetzen).
                </figcaption>
            </figure>
        </article>
    );
}
