import Link from "next/link";
import MetricCard from "@/components/MetricCard";

const sampleFindings = [
  { title: "No MFA", severity: "High", owner: "Security", dueDate: "2026-04-20" },
  { title: "Encryption at rest unclear", severity: "High", owner: "Vendor", dueDate: "2026-04-18" },
  { title: "No breach timeline", severity: "Medium", owner: "Legal", dueDate: "2026-04-25" }
];

export default function DashboardPage() {
  return (
    <main style={{ display: "grid", gap: 20 }}>
      <section className="card">
        <h1 className="page-title">Risk dashboard</h1>
        <p className="page-subtitle">
          Use this starter to assess vendors, review findings, and track remediation.
        </p>
        <div style={{ display: "flex", gap: 12, marginTop: 16, flexWrap: "wrap" }}>
          <Link href="/new-assessment" className="button-primary">Start new assessment</Link>
          <Link href="/risk-register" className="button-secondary">Open risk register</Link>
        </div>
      </section>

      <section className="grid-cards">
        <MetricCard label="Open assessments" value="12" />
        <MetricCard label="High risks" value="7" />
        <MetricCard label="Overdue actions" value="3" />
        <MetricCard label="Approved vendors" value="18" />
      </section>

      <section className="card">
        <h2 className="section-title">Recent findings</h2>
        <table className="table">
          <thead>
            <tr>
              <th>Finding</th>
              <th>Severity</th>
              <th>Owner</th>
              <th>Due date</th>
            </tr>
          </thead>
          <tbody>
            {sampleFindings.map((item) => (
              <tr key={item.title}>
                <td>{item.title}</td>
                <td>{item.severity}</td>
                <td>{item.owner}</td>
                <td>{item.dueDate}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </main>
  );
}
