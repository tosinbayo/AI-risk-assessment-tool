import Link from "next/link";

const links = [
  { href: "/", label: "Dashboard" },
  { href: "/new-assessment", label: "New Assessment" },
  { href: "/risk-register", label: "Risk Register" }
];

export default function NavBar() {
  return (
    <header className="card" style={{ marginBottom: 24, padding: 16 }}>
      <div style={{ display: "flex", gap: 12, justifyContent: "space-between", alignItems: "center", flexWrap: "wrap" }}>
        <div>
          <div style={{ fontSize: 20, fontWeight: 800 }}>RiskLens AI</div>
          <div style={{ color: "#6b7280", marginTop: 4 }}>Vendor risk assessment frontend starter</div>
        </div>
        <nav style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
          {links.map((link) => (
            <Link key={link.href} href={link.href} className="button-secondary">
              {link.label}
            </Link>
          ))}
        </nav>
      </div>
    </header>
  );
}
