import { useEffect } from "react";
import { Route, Routes, useLocation } from "react-router-dom";
import Layout from "./components/Layout";
import Home from "./pages/Home";
import Barrieren from "./pages/Barrieren";
import Loesungen from "./pages/Loesungen";
import Ueber from "./pages/Ueber";

/**
 * Setzt nach jedem Routenwechsel den Fokus auf das <main>-Element,
 * damit Screenreader die neue Seite konsistent ansagen.
 */
function FocusOnNavigate() {
    const { pathname } = useLocation();
    useEffect(() => {
        const main = document.getElementById("main");
        if (main) main.focus();
    }, [pathname]);
    return null;
}

export default function App() {
    return (
        <Layout>
            <FocusOnNavigate />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/barrieren" element={<Barrieren />} />
                <Route path="/loesungen" element={<Loesungen />} />
                <Route path="/ueber" element={<Ueber />} />
            </Routes>
        </Layout>
    );
}
