import { NavLink } from "react-router-dom";

const items = [
    { to: "/",          label: "Startseite",          end: true },
    { to: "/barrieren", label: "Barrieren-Beispiel" },
    { to: "/loesungen", label: "Lösungs-Beispiel" },
    { to: "/ueber",     label: "Über diese App" }
] as const;

export default function NavMenu() {
    return (
        <nav className="bfw-nav" aria-label="Hauptnavigation">
            <div className="container">
                <ul className="nav">
                    {items.map((it) => (
                        <li className="nav-item" key={it.to}>
                            <NavLink
                                to={it.to}
                                end={"end" in it ? it.end : false}
                                className={({ isActive }) =>
                                    "nav-link" + (isActive ? " active" : "")
                                }
                            >
                                {it.label}
                            </NavLink>
                        </li>
                    ))}
                </ul>
            </div>
        </nav>
    );
}
