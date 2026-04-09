export type Finding = {
  title: string;
  severity: string;
  description: string;
  recommendation: string;
  framework_mapping: string[];
};

export type ScoreBreakdown = {
  inherent_risk: number;
  control_strength: number;
  evidence_confidence: number;
  residual_risk: number;
  risk_level: string;
};

export type AssessmentOutput = {
  vendor_name: string;
  service_description: string;
  score_breakdown: ScoreBreakdown;
  findings: Finding[];
  top_risk_flags: string[];
};

export type AssessmentInput = {
  vendor_name: string;
  service_description: string;
  assessor_name?: string;
  regulatory_scope: string[];
  answers: Record<string, number>;
  evidence: Record<string, string>;
};
