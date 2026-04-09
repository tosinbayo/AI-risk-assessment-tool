from typing import List, Literal, Optional
from pydantic import BaseModel, Field


AnswerValue = Literal[1, 2, 3, 4, 5]
EvidenceStrength = Literal["strong", "medium", "weak", "missing"]


class QuestionnaireAnswers(BaseModel):
    q1_data_type: AnswerValue = Field(..., description="1=Public, 2=Internal, 4=Confidential, 5=Sensitive")
    q2_business_criticality: AnswerValue
    q3_customer_data_access: AnswerValue
    q4_internet_facing: AnswerValue
    q5_regulated_regions: AnswerValue
    q6_mfa: AnswerValue
    q7_rbac: AnswerValue
    q8_privileged_monitoring: AnswerValue
    q9_encryption_at_rest: AnswerValue
    q10_encryption_in_transit: AnswerValue
    q11_data_retention_policy: AnswerValue
    q12_incident_response_plan: AnswerValue
    q13_breach_notification_timeline: AnswerValue
    q14_log_monitoring: AnswerValue
    q15_certification: AnswerValue
    q16_security_audits: AnswerValue
    q17_subprocessor_disclosure: AnswerValue
    q18_bcdr: AnswerValue
    q19_backups_tested: AnswerValue
    q20_secure_hosting: AnswerValue


class EvidenceSummary(BaseModel):
    encryption_at_rest: EvidenceStrength = "missing"
    encryption_in_transit: EvidenceStrength = "missing"
    access_control: EvidenceStrength = "missing"
    incident_response: EvidenceStrength = "missing"
    logging_monitoring: EvidenceStrength = "missing"
    certification: EvidenceStrength = "missing"
    backups: EvidenceStrength = "missing"
    hosting_security: EvidenceStrength = "missing"


class AssessmentInput(BaseModel):
    vendor_name: str
    service_description: str
    assessor_name: Optional[str] = None
    regulatory_scope: List[str] = []
    answers: QuestionnaireAnswers
    evidence: EvidenceSummary


class FindingOut(BaseModel):
    title: str
    severity: str
    description: str
    recommendation: str
    framework_mapping: List[str]


class ScoreBreakdown(BaseModel):
    inherent_risk: float
    control_strength: float
    evidence_confidence: float
    residual_risk: float
    risk_level: str


class AssessmentOutput(BaseModel):
    vendor_name: str
    service_description: str
    score_breakdown: ScoreBreakdown
    findings: List[FindingOut]
    top_risk_flags: List[str]


class SavedAssessmentResponse(AssessmentOutput):
    assessment_id: int


class FileUploadResponse(BaseModel):
    file_name: str
    content_type: Optional[str] = None
    saved_path: str


class ExtractEvidenceRequest(BaseModel):
    file_path: str


class ExtractEvidenceResponse(BaseModel):
    file_path: str
    extracted_text_preview: str
    evidence_summary: EvidenceSummary
    notes: List[str]
