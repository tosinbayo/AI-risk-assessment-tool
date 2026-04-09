
from dataclasses import dataclass
from typing import List


@dataclass
class QuestionnaireAnswers:
    answers: List[int]


@dataclass
class EvidenceSummary:
    encryption_at_rest: str
    encryption_in_transit: str
    access_control: str
    incident_response: str
    logging_monitoring: str
    certification: str
    backups: str
    hosting_security: str


@dataclass
class ScoreBreakdown:
    section: str
    score: float
    weight: float
    weighted_score: float


@dataclass
class AssessmentInput:
    answers: List[int]
    evidence_text: str = ""


@dataclass
class AssessmentOutput:
    overall_score: float
    risk_level: str
    score_breakdown: List[ScoreBreakdown]
    top_risk_flags: List[str]
    findings: List[str]
