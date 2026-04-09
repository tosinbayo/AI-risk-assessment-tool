from typing import List
from app.mappings import QUESTION_FRAMEWORK_MAP
from app.schemas import FindingOut, QuestionnaireAnswers


def build_finding(title: str, severity: str, description: str, recommendation: str, framework_keys: List[str]) -> FindingOut:
    frameworks = []
    for key in framework_keys:
        frameworks.extend(QUESTION_FRAMEWORK_MAP.get(key, []))
    frameworks = sorted(set(frameworks))
    return FindingOut(
        title=title,
        severity=severity,
        description=description,
        recommendation=recommendation,
        framework_mapping=frameworks,
    )


def generate_findings(answers: QuestionnaireAnswers) -> List[FindingOut]:
    findings: List[FindingOut] = []

    if answers.q6_mfa == 5:
        findings.append(build_finding(
            "Multi-factor authentication is not enforced",
            "High",
            "The absence of MFA increases the likelihood of account compromise, especially for privileged or remote access paths.",
            "Require MFA across all user and administrative accounts before onboarding or renewal.",
            ["q6_mfa"],
        ))

    if answers.q7_rbac in [3, 5]:
        findings.append(build_finding(
            "Role-based access control is incomplete or missing",
            "Medium" if answers.q7_rbac == 3 else "High",
            "Weak access segmentation may lead to excessive privileges and poor separation of duties.",
            "Implement formal RBAC with least-privilege role definitions and periodic access reviews.",
            ["q7_rbac"],
        ))

    if answers.q9_encryption_at_rest == 5:
        findings.append(build_finding(
            "No evidence of encryption at rest",
            "Critical",
            "Sensitive or customer data may be exposed if storage systems are compromised.",
            "Require encryption at rest using recognized standards such as AES-256, including documented key management controls.",
            ["q9_encryption_at_rest"],
        ))
    elif answers.q9_encryption_at_rest == 4:
        findings.append(build_finding(
            "Encryption at rest is unclear",
            "High",
            "Documentation does not provide enough assurance that stored data is encrypted.",
            "Obtain explicit documentation of encryption at rest, scope, standards used, and key management procedures.",
            ["q9_encryption_at_rest"],
        ))

    if answers.q10_encryption_in_transit == 5:
        findings.append(build_finding(
            "Data encryption in transit is not confirmed",
            "High",
            "Data transmitted across networks may be susceptible to interception or manipulation.",
            "Require TLS-based encryption in transit for all communications carrying sensitive data.",
            ["q10_encryption_in_transit"],
        ))

    if answers.q12_incident_response_plan == 5:
        findings.append(build_finding(
            "No incident response plan",
            "High",
            "The vendor may be unable to detect, contain, investigate, and recover from security incidents in a timely manner.",
            "Require a documented incident response plan with roles, escalation paths, testing cadence, and communication procedures.",
            ["q12_incident_response_plan"],
        ))

    if answers.q13_breach_notification_timeline == 5:
        findings.append(build_finding(
            "Breach notification timeline is not defined",
            "High",
            "The absence of a defined notification timeline creates legal, operational, and contractual exposure during incidents.",
            "Require breach notification commitments aligned to applicable laws and contractual obligations.",
            ["q13_breach_notification_timeline"],
        ))

    if answers.q14_log_monitoring == 5:
        findings.append(build_finding(
            "Security logging and monitoring are insufficient",
            "High",
            "Without monitoring, malicious activity may remain undetected for longer periods.",
            "Implement centralized log collection, alerting, and regular review of security events.",
            ["q14_log_monitoring"],
        ))

    if answers.q15_certification == 5:
        findings.append(build_finding(
            "No independent security assurance certification",
            "Medium",
            "The vendor does not demonstrate recognized external assurance such as SOC 2 or ISO 27001.",
            "Request alternative assurance evidence or require a roadmap toward independent certification.",
            ["q15_certification"],
        ))

    if answers.q17_subprocessor_disclosure == 5:
        findings.append(build_finding(
            "Subprocessors are not disclosed",
            "High",
            "Opaque subprocessor relationships may create hidden legal, security, and geographic risk exposure.",
            "Require a current subprocessor list, locations, services provided, and notification commitments for changes.",
            ["q17_subprocessor_disclosure"],
        ))

    if answers.q18_bcdr == 5 or answers.q19_backups_tested == 5:
        findings.append(build_finding(
            "Business continuity and backup resilience are weak",
            "High",
            "Operational recovery capabilities may be insufficient during outages, ransomware incidents, or infrastructure failure.",
            "Require formal BCDR documentation, tested backup restoration procedures, and recovery objectives.",
            ["q18_bcdr", "q19_backups_tested"],
        ))

    if answers.q20_secure_hosting == 5:
        findings.append(build_finding(
            "Hosting environment security is inadequate",
            "High",
            "The underlying infrastructure may lack sufficient hardening, monitoring, or cloud security controls.",
            "Require evidence of secure hosting architecture, hardening standards, vulnerability management, and cloud security baselines.",
            ["q20_secure_hosting"],
        ))

    return findings


def get_top_risk_flags(answers: QuestionnaireAnswers) -> List[str]:
    flags: List[str] = []

    if answers.q6_mfa == 5:
        flags.append("No MFA")
    if answers.q9_encryption_at_rest == 5:
        flags.append("No encryption at rest")
    if answers.q12_incident_response_plan == 5:
        flags.append("No incident response plan")
    if answers.q13_breach_notification_timeline == 5:
        flags.append("No breach notification timeline")
    if answers.q1_data_type == 5 and answers.q15_certification == 5:
        flags.append("Sensitive data with no external assurance")

    return flags
