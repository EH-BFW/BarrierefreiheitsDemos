export default function Loesungen() {
    return (
        <article>
            <h1 className="text-bfw-red">Lösungs-Beispiel</h1>
            <p>
                Identische fünf Elemente – diesmal <strong>barrierefrei umgesetzt</strong>.
                Hinweise zur jeweiligen Lösung stehen direkt unter dem Beispiel.
            </p>

            {/* 1 */}
            <section className="demo">
                <h2 className="h5">1. Beschriftetes Eingabefeld</h2>
                <label htmlFor="name" className="form-label">Vor- und Nachname</label>
                <input id="name" type="text" autoComplete="name"
                       className="form-control" style={{ maxWidth: 320 }} />
                <p className="hint">
                    Lösung: explizites <code>&lt;label htmlFor&gt;</code> verbindet Beschriftung und Feld.
                </p>
            </section>

            {/* 2 */}
            <section className="demo">
                <h2 className="h5">2. Lesbares Feld mit Tastaturfokus</h2>
                <label htmlFor="kdnr" className="form-label">Kundennummer</label>
                <input id="kdnr" type="text" defaultValue="K-4711" readOnly
                       className="form-control" style={{ maxWidth: 320 }} />
                <p className="hint">
                    Lösung: <code>readOnly</code> statt <code>disabled</code> – fokussierbar und lesbar.
                </p>
            </section>

            {/* 3 */}
            <section className="demo">
                <h2 className="h5">3. Beschriftetes Diagramm mit Textalternative</h2>
                <figure>
                    <div
                        className="chart"
                        role="img"
                        tabIndex={0}
                        aria-labelledby="chart-title"
                        aria-describedby="chart-desc"
                    >
                        <svg viewBox="0 0 200 80" width="200" height="80" aria-hidden="true">
                            <rect x="10"  y="40" width="20" height="30" fill="#C8102E" />
                            <rect x="40"  y="20" width="20" height="50" fill="#C8102E" />
                            <rect x="70"  y="10" width="20" height="60" fill="#C8102E" />
                            <rect x="100" y="30" width="20" height="40" fill="#C8102E" />
                            <rect x="130" y="25" width="20" height="45" fill="#C8102E" />
                        </svg>
                    </div>
                    <figcaption id="chart-title">Umsätze Q1–Q5 in T€</figcaption>
                    <p id="chart-desc" className="visually-hidden">
                        Balkendiagramm: Q1 30, Q2 50, Q3 60, Q4 40, Q5 45 Tausend Euro.
                    </p>
                </figure>
                <p className="hint">
                    Lösung: <code>role="img"</code> +
                    <code>aria-labelledby</code> / <code>aria-describedby</code>;
                    SVG selbst per <code>aria-hidden</code> ausgeblendet.
                </p>
            </section>

            {/* 4 */}
            <section className="demo">
                <h2 className="h5">4. Schaltfläche mit ausreichendem Kontrast</h2>
                <button className="btn btn-bfw-primary">Speichern</button>
                <p className="hint">
                    Lösung: WCAG-AA-konformes Kontrastverhältnis ≥ 4,5:1
                    (weiß auf BFW-Rot #C8102E).
                </p>
            </section>

            {/* 5 */}
            <section className="demo">
                <h2 className="h5">5. Icon-Schaltfläche mit zugänglichem Namen</h2>
                <button
                    type="button"
                    className="btn btn-outline-secondary icon-btn"
                    aria-label="Eintrag löschen"
                >
                    <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">
                        <path d="M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14"
                              fill="none" stroke="#333" strokeWidth="2" />
                    </svg>
                </button>
                <p className="hint">
                    Lösung: <code>aria-label</code> liefert den zugänglichen Namen;
                    das SVG ist als rein dekorativ markiert.
                </p>
            </section>
        </article>
    );
}
