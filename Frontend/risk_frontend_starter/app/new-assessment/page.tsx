"use client";

import { FormEvent, useMemo, useState } from "react";
import { analyzeAssessment } from "@/lib/api";
import { AssessmentOutput, AssessmentInput } from "@/lib/types";
import { evidenceFields, evidenceOptions, questionGroups } from "@/lib/constants";
import AssessmentResults from "@/components/AssessmentResults";

const initialAnswers = Object.fromEntries(
  questionGroups.flatMap((group) => group.fields.map((field) => [field.key, field.options[0].value]))
);

const initialEvidence = Object.fromEntries(
  evidenceFields.map((field) => [field, "missing"])
);

export default function NewAssessmentPage() {
  const [vendorName, setVendorName] = useState("");
  const [serviceDescription, setServiceDescription] = useState("");
  const [assessorName, setAssessorName] = useState("");
  const [regulatoryScope, setRegulatoryScope] = useState("GDPR, SOC 2");
  const [answers, setAnswers] = useState<Record<string, number>>(initialAnswers);
  const [evidence, setEvidence] = useState<Record<string, string>>(initialEvidence);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [result, setResult] = useState<AssessmentOutput | null>(null);

  const canSubmit = useMemo(() => vendorName.trim() && serviceDescription.trim(), [vendorName, serviceDescription]);

  const onSubmit = async (event: FormEvent) => {
    event.preventDefault();
    setLoading(true);
    setError("");
    setResult(null);

    const payload: AssessmentInput = {
      vendor_name: vendorName,
      service_description: serviceDescription,
      assessor_name: assessorName || undefined,
      regulatory_scope: regulatoryScope
        .split(",")
        .map((item) => item.trim())
        .filter(Boolean),
      answers,
      evidence
    };

    try {
      const response = await analyzeAssessment(payload);
      setResult(response);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main style={{ display: "grid", gap: 20 }}>
      <section className="card">
        <h1 className="page-title">New assessment</h1>
        <p className="page-subtitle">Fill the form below to send a vendor assessment to the backend.</p>
      </section>

      <form onSubmit={onSubmit} style={{ display: "grid", gap: 20 }}>
        <section className="card">
          <h2 className="section-title">Vendor details</h2>
          <div className="form-grid">
            <div>
              <label className="label">Vendor name</label>
              <input className="field" value={vendorName} onChange={(e) => setVendorName(e.target.value)} />
            </div>
            <div>
              <label className="label">Assessor name</label>
              <input className="field" value={assessorName} onChange={(e) => setAssessorName(e.target.value)} />
            </div>
            <div style={{ gridColumn: "1 / -1" }}>
              <label className="label">Service description</label>
              <textarea className="field" rows={4} value={serviceDescription} onChange={(e) => setServiceDescription(e.target.value)} />
            </div>
            <div style={{ gridColumn: "1 / -1" }}>
              <label className="label">Regulatory scope</label>
              <input className="field" value={regulatoryScope} onChange={(e) => setRegulatoryScope(e.target.value)} placeholder="GDPR, SOC 2, ISO 27001" />
            </div>
          </div>
        </section>

        {questionGroups.map((group) => (
          <section className="card" key={group.title}>
            <h2 className="section-title">{group.title}</h2>
            <div className="form-grid">
              {group.fields.map((field) => (
                <div key={field.key}>
                  <label className="label">{field.label}</label>
                  <select
                    className="field"
                    value={String(answers[field.key])}
                    onChange={(e) => setAnswers((prev) => ({ ...prev, [field.key]: Number(e.target.value) }))}
                  >
                    {field.options.map((option) => (
                      <option key={`${field.key}-${option.value}`} value={option.value}>
                        {option.label} ({option.value})
                      </option>
                    ))}
                  </select>
                </div>
              ))}
            </div>
          </section>
        ))}

        <section className="card">
          <h2 className="section-title">Evidence summary</h2>
          <div className="form-grid">
            {evidenceFields.map((field) => (
              <div key={field}>
                <label className="label">{field.replaceAll("_", " ")}</label>
                <select
                  className="field"
                  value={evidence[field]}
                  onChange={(e) => setEvidence((prev) => ({ ...prev, [field]: e.target.value }))}
                >
                  {evidenceOptions.map((option) => (
                    <option key={`${field}-${option.value}`} value={option.value}>
                      {option.label}
                    </option>
                  ))}
                </select>
              </div>
            ))}
          </div>
        </section>

        <div style={{ display: "flex", gap: 12, flexWrap: "wrap" }}>
          <button type="submit" className="button-primary" disabled={!canSubmit || loading}>
            {loading ? "Analyzing..." : "Analyze assessment"}
          </button>
        </div>

        {error && (
          <div className="card" style={{ borderColor: "#fca5a5", background: "#fef2f2" }}>
            <strong>Request failed</strong>
            <div style={{ marginTop: 8 }}>{error}</div>
          </div>
        )}

        {result && (
          <section className="card">
            <h2 className="section-title">Assessment result</h2>
            <AssessmentResults data={result} />
          </section>
        )}
      </form>
    </main>
  );
}
