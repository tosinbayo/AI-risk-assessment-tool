from pathlib import Path
from app.schemas import EvidenceSummary


def extract_text_preview(file_path: str, max_chars: int = 1200) -> str:
    path = Path(file_path)
    if not path.exists():
        return ""

    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return "Binary or unsupported file preview not available in stub."

    return text[:max_chars]


def infer_evidence_from_text(text: str) -> tuple[EvidenceSummary, list[str]]:
    lowered = text.lower()
    notes = []

    evidence = EvidenceSummary(
        encryption_at_rest="strong" if "encryption at rest" in lowered else "missing",
        encryption_in_transit="strong" if ("tls" in lowered or "encryption in transit" in lowered) else "missing",
        access_control="medium" if ("mfa" in lowered or "role-based access control" in lowered or "rbac" in lowered) else "missing",
        incident_response="medium" if "incident response" in lowered else "missing",
        logging_monitoring="medium" if ("siem" in lowered or "logging" in lowered or "monitoring" in lowered) else "missing",
        certification="medium" if ("soc 2" in lowered or "iso 27001" in lowered) else "missing",
        backups="medium" if "backup" in lowered else "missing",
        hosting_security="medium" if ("aws" in lowered or "azure" in lowered or "gcp" in lowered or "hardened" in lowered) else "missing",
    )

    if evidence.encryption_at_rest == "missing":
        notes.append("No direct reference to encryption at rest found in stub scan.")
    if evidence.certification == "missing":
        notes.append("No direct reference to SOC 2 or ISO 27001 found in stub scan.")
    if evidence.incident_response == "missing":
        notes.append("No direct reference to incident response found in stub scan.")

    return evidence, notes
