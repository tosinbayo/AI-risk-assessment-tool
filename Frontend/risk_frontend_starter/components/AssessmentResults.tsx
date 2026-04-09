import { AssessmentOutput } from "@/lib/types";

function getRiskBadgeStyle(level: string) {
  switch (level) {
    case "Low":
      return { background: "#ecfdf5", borderColor: "#a7f3d0" };
    case "Medium":
      return { background: "#fffbeb", borderColor: "#fde68a" };
    case "High":
      return { background: "#fff7ed", borderColor: "#fdba74" };
    default:
      return { background: "#fef2f2", borderColor: "#fca5a5" };
  }
}

export default function AssessmentResults({ data }: { data: AssessmentOutput }) {
  const riskStyle = getRiskBadgeStyle(data.score_breakdown.risk_level);

  return (
    <div style={{ display: "grid", gap: 16 }}>
      <div className="grid-cards">
        <div className="card">
          <div className="metric-value">{data.score_breakdown.inherent_risk}</div>
          <div className="metric-label">Inherent Risk</div>
        </div>
        <div className="card">
          <div className="metric-value">{data.score_breakdown.control_strength}</div>
          <div className="metric-label">Control Strength</div>
        </div>
        <div className="card">
          <div className="metric-value">{data.score_breakdown.evidence_confidence}</div>
          <div className="metric-label">Evidence Confidence</div>
        </div>
        <div className="card">
          <div className="metric-value">{data.score_breakdown.residual_risk}</div>
          <div className="metric-label">Residual Risk</div>
          <div className="badge" style={{ marginTop: 12, ...riskStyle }}>
            {data.score_breakdown.risk_level}
          </div>
        </div>
      </div>

      <div className="card">
        <h3 className="section-title">Top Risk Flags</h3>
        <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
          {data.top_risk_flags.length === 0 ? (
            <span style={{ color: "#6b7280" }}>No major flags triggered.</span>
          ) : (
            data.top_risk_flags.map((flag) => (
              <span key={flag} className="badge">{flag}</span>
            ))
          )}
        </div>
      </div>

      <div className="card">
        <h3 className="section-title">Findings</h3>
        <div style={{ display: "grid", gap: 12 }}>
          {data.findings.map((finding, index) => (
            <div key={`${finding.title}-${index}`} style={{ border: "1px solid #e5e7eb", borderRadius: 14, padding: 16 }}>
              <div style={{ display: "flex", justifyContent: "space-between", gap: 12, flexWrap: "wrap" }}>
                <strong>{finding.title}</strong>
                <span className="badge">{finding.severity}</span>
              </div>
              <p style={{ marginTop: 12, marginBottom: 8 }}>{finding.description}</p>
              <p style={{ marginTop: 0, marginBottom: 10 }}>
                <strong>Recommendation:</strong> {finding.recommendation}
              </p>
              <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
                {finding.framework_mapping.map((item) => (
                  <span key={item} className="badge">{item}</span>
                ))}
              </div>
            </div>
          ))}
          {data.findings.length === 0 && (
            <div style={{ color: "#6b7280" }}>No findings generated.</div>
          )}
        </div>
      </div>
    </div>
  );
}
