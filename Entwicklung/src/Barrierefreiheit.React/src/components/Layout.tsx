import type { PropsWithChildren } from "react";
import NavMenu from "./NavMenu";

export default function Layout({ children }: PropsWithChildren) {
    return (
        <div className="d-flex flex-column min-vh-100">
            <header className="bfw-header" role="banner">
                <div className="container d-flex align-items-center py-2">
                    <span className="bfw-mark me-2" aria-hidden="true" />
                    <span className="fw-semibold text-white">
                        BFW Würzburg · Barrierefreiheit (React)
                    </span>
                </div>
            </header>

            <NavMenu />

            <main
                id="main"
                role="main"
                tabIndex={-1}
                className="container my-4 flex-grow-1"
            >
                {children}
            </main>

            <footer className="bfw-footer" role="contentinfo">
                <div className="container py-2">
                    <small>
                        © {new Date().getFullYear()} BFW Würzburg gGmbH – Beispiel-App
                        zur digitalen Barrierefreiheit (React + Bootstrap)
                    </small>
                </div>
            </footer>
        </div>
    );
}
