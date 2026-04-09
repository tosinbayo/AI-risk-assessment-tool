
from dataclasses import dataclass
from typing import List

@dataclass
class QuestionnaireAnswers:
    answers: List[int]

@dataclass
class EvidenceSummary:
    scores: List[float]
