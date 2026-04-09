from app.schemas import QuestionnaireAnswers, EvidenceSummary


def avg(values):
    return sum(values) / len(values)


def calculate_inherent_risk(answers: QuestionnaireAnswers) -> float:
    return round(
        (0.3 * answers.q1_data_type) +
        (0.3 * answers.q2_business_criticality) +
        (0.2 * answers.q3_customer_data_access) +
        (0.1 * answers.q4_internet_facing) +
        (0.1 * answers.q5_regulated_regions),
        2,
    )


def calculate_control_strength(answers: QuestionnaireAnswers) -> float:
    access_control = avg([answers.q6_mfa, answers.q7_rbac, answers.q8_privileged_monitoring])
    data_protection = avg([answers.q9_encryption_at_rest, answers.q10_encryption_in_transit, answers.q11_data_retention_policy])
    security_ops = avg([answers.q12_incident_response_plan, answers.q13_breach_notification_timeline, answers.q14_log_monitoring])
    compliance = avg([answers.q15_certification, answers.q16_security_audits, answers.q17_subprocessor_disclosure])
    resilience = avg([answers.q18_bcdr, answers.q19_backups_tested, answers.q20_secure_hosting])

    return round(
        (0.25 * access_control) +
        (0.25 * data_protection) +
        (0.20 * security_ops) +
        (0.15 * compliance) +
        (0.15 * resilience),
        2,
    )


def evidence_strength_to_score(value: str) -> int:
    mapping = {
        "strong": 1,
        "medium": 3,
        "weak": 4,
        "missing": 5,
    }
    return mapping[value]


def calculate_evidence_confidence(evidence: EvidenceSummary) -> float:
    scores = [
        evidence_strength_to_score(evidence.encryption_at_rest),
        evidence_strength_to_score(evidence.encryption_in_transit),
        evidence_strength_to_score(evidence.access_control),
        evidence_strength_to_score(evidence.incident_response),
        evidence_strength_to_score(evidence.logging_monitoring),
        evidence_strength_to_score(evidence.certification),
        evidence_strength_to_score(evidence.backups),
        evidence_strength_to_score(evidence.hosting_security),
    ]
    return round(avg(scores), 2)


def calculate_residual_risk(inherent_risk: float, control_strength: float, evidence_confidence: float) -> float:
    control_gap = 6 - control_strength
    score = inherent_risk + (control_gap * 0.6) + (evidence_confidence * 0.4)
    normalized = min(score / 2, 5.0)
    return round(normalized, 2)


def classify_risk_level(score: float) -> str:
    if 1.0 <= score <= 2.0:
        return "Low"
    if 2.0 < score <= 3.0:
        return "Medium"
    if 3.0 < score <= 4.0:
        return "High"
    return "Critical"


def get_score_breakdown(answers: QuestionnaireAnswers, evidence: EvidenceSummary) -> dict:
    inherent_risk = calculate_inherent_risk(answers)
    control_strength = calculate_control_strength(answers)
    evidence_confidence = calculate_evidence_confidence(evidence)
    residual_risk = calculate_residual_risk(inherent_risk, control_strength, evidence_confidence)
    risk_level = classify_risk_level(residual_risk)

    return {
        "inherent_risk": inherent_risk,
        "control_strength": control_strength,
        "evidence_confidence": evidence_confidence,
        "residual_risk": residual_risk,
        "risk_level": risk_level,
    }
