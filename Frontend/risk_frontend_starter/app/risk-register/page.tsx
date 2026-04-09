const rows = [
  {
    vendor: "Acme Cloud Analytics",
    risk: "No MFA",
    severity: "High",
    owner: "Security",
    status: "Open",
    dueDate: "2026-04-20"
  },
  {
    vendor: "Northwind AI",
    risk: "Incident response plan missing",
    severity: "High",
    owner: "Vendor",
    status: "In progress",
    dueDate: "2026-04-28"
  },
  {
    vendor: "BluePeak CRM",
    risk: "Subprocessors not disclosed",
    severity: "Medium",
    owner: "Legal",
    status: "Open",
    dueDate: "2026-05-05"
  }
];

export default function RiskRegisterPage() {
  return (
    <main style={{ display: "grid", gap: 20 }}>
      <section className="card">
        <h1 className="page-title">Risk register</h1>
        <p className="page-subtitle">Starter table for tracking findings, owners, due dates, and status.</p>
      </section>

      <section className="card">
        <table className="table">
          <thead>
            <tr>
              <th>Vendor</th>
              <th>Risk</th>
              <th>Severity</th>
              <th>Owner</th>
              <th>Status</th>
              <th>Due date</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((row) => (
              <tr key={`${row.vendor}-${row.risk}`}>
                <td>{row.vendor}</td>
                <td>{row.risk}</td>
                <td>{row.severity}</td>
                <td>{row.owner}</td>
                <td>{row.status}</td>
                <td>{row.dueDate}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </main>
  );
}
