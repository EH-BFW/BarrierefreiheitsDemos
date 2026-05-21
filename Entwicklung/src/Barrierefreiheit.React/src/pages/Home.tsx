export default function Home() {
    return (
        <article>
            <h1 className="text-bfw-red">Barrierefreiheit – React-Beispiel</h1>
            <p className="lead">
                Diese React-/Bootstrap-App zeigt typische digitale Barrieren für
                Screenreader-Nutzende (besonders blinde Menschen) – und stellt
                die gleichen Beispiele in der Variante <strong>barrierefrei umgesetzt</strong>{" "}
                gegenüber.
            </p>
            <p>
                Wechseln Sie über das Menü zwischen <strong>Barrieren-Beispiel</strong>{" "}
                und <strong>Lösungs-Beispiel</strong>, um den Unterschied direkt mit
                NVDA oder JAWS zu erleben.
            </p>

            <figure className="my-4">
                <svg viewBox="0 0 640 320" role="img"
                     aria-label="Browserfenster mit semantischem HTML, Fokus-Indikator und Screenreader-Hinweis."
                     style={{ width: "100%", maxWidth: 640, height: "auto", border: "1px solid #E9ECEF" }}>
                    <rect width="640" height="320" fill="#F5F6F8" />
                    <rect x="40" y="30" width="560" height="260" rx="8" fill="#FFF" stroke="#1F2A36" strokeWidth="2" />
                    <rect x="40" y="30" width="560" height="34" rx="8" fill="#1F2A36" />
                    <circle cx="62" cy="47" r="5" fill="#C8102E" />
                    <circle cx="80" cy="47" r="5" fill="#F1C40F" />
                    <circle cx="98" cy="47" r="5" fill="#2ECC71" />
                    <rect x="60" y="80"  width="200" height="14" fill="#C8102E" />
                    <rect x="60" y="110" width="520" height="8" fill="#5A6470" />
                    <rect x="60" y="124" width="500" height="8" fill="#5A6470" />
                    <rect x="60" y="138" width="450" height="8" fill="#5A6470" />
                    <rect x="60" y="170" width="160" height="32" fill="#C8102E" rx="4" />
                    <text x="80" y="191" fill="#fff" fontFamily="Segoe UI, sans-serif" fontSize="14" fontWeight="600">Speichern</text>
                    <rect x="240" y="170" width="160" height="32" fill="#FFF" stroke="#0050B3" strokeWidth="3" rx="4" />
                    <text x="260" y="191" fill="#0050B3" fontFamily="Segoe UI, sans-serif" fontSize="14">Fokus sichtbar</text>
                    <text x="60" y="240" fill="#1F2A36" fontFamily="Segoe UI, sans-serif" fontSize="13">
                        Screenreader: "Speichern, Schaltfläche"
                    </text>
                </svg>
                <figcaption className="text-muted mt-2">
                    React 18 + Bootstrap 5 + React Router – statische SPA.
                </figcaption>
            </figure>
        </article>
    );
}
