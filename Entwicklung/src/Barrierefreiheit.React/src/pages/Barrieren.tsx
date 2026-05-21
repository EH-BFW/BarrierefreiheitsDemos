export default function Barrieren() {
    return (
        <article>
            <h1 className="text-bfw-red">Barrieren-Beispiel</h1>
            <p>
                Achtung: Diese Seite ist <strong>bewusst nicht barrierefrei</strong>.
                Sie demonstriert typische Hürden für Screenreader-Nutzende.
            </p>

            {/* 1: Unbeschriftetes Eingabefeld */}
            <section className="demo">
                <h2 className="h5">1. Unbeschriftetes Eingabefeld</h2>
                {/* BARRIERE: weder label noch aria-label */}
                <input type="text" className="form-control" style={{ maxWidth: 320 }} />
            </section>

            {/* 2: disabled statt readonly */}
            <section className="demo">
                <h2 className="h5">2. Per Tastatur nicht erreichbares Feld (disabled statt readonly)</h2>
                <label>
                    Kundennummer
                    <input
                        type="text"
                        defaultValue="K-4711"
                        disabled
                        className="form-control"
                        style={{ maxWidth: 320 }}
                    />
                </label>
            </section>

            {/* 3: Fokussierbar aber unbeschriftet */}
            <section className="demo">
                <h2 className="h5">3. Fokussierbares, aber unbeschriftetes Diagramm</h2>
                <div className="chart" tabIndex={0}>
                    <svg viewBox="0 0 200 80" width="200" height="80">
                        <rect x="10"  y="40" width="20" height="30" fill="#888" />
                        <rect x="40"  y="20" width="20" height="50" fill="#888" />
                        <rect x="70"  y="10" width="20" height="60" fill="#888" />
                        <rect x="100" y="30" width="20" height="40" fill="#888" />
                        <rect x="130" y="25" width="20" height="45" fill="#888" />
                    </svg>
                </div>
            </section>

            {/* 4: Kontrastarmer Button */}
            <section className="demo">
                <h2 className="h5">4. Schaltfläche mit zu schwachem Kontrast</h2>
                <button className="btn low-contrast">Speichern</button>
            </section>

            {/* 5: Icon-Schaltfläche ohne Beschriftung */}
            <section className="demo">
                <h2 className="h5">5. Icon-Schaltfläche ohne Beschriftung</h2>
                <button className="btn btn-outline-secondary icon-btn">
                    <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true">
                        <path d="M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14"
                              fill="none" stroke="#333" strokeWidth="2" />
                    </svg>
                </button>
            </section>
        </article>
    );
}
