export const ANSWER_OPTIONS = {
  yesNoRisk: [
    { label: "Yes", value: 1 },
    { label: "Partial / Unclear", value: 3 },
    { label: "No", value: 5 }
  ]
};

export const questionGroups = [
  {
    title: "Section A — Data & Business Impact",
    fields: [
      {
        key: "q1_data_type",
        label: "What type of data will the vendor process?",
        options: [
          { label: "Public", value: 1 },
          { label: "Internal", value: 2 },
          { label: "Confidential", value: 4 },
          { label: "Sensitive / PII / Financial / Health", value: 5 }
        ]
      },
      {
        key: "q2_business_criticality",
        label: "What is the business criticality of this vendor?",
        options: [
          { label: "Low", value: 1 },
          { label: "Medium", value: 3 },
          { label: "High", value: 5 }
        ]
      },
      {
        key: "q3_customer_data_access",
        label: "Will the vendor have access to customer data?",
        options: [
          { label: "No", value: 1 },
          { label: "Limited", value: 3 },
          { label: "Full access", value: 5 }
        ]
      },
      {
        key: "q4_internet_facing",
        label: "Is the service internet-facing?",
        options: [
          { label: "No", value: 1 },
          { label: "Yes", value: 5 }
        ]
      },
      {
        key: "q5_regulated_regions",
        label: "Does the vendor operate in regulated regions?",
        options: [
          { label: "No", value: 1 },
          { label: "Yes", value: 5 }
        ]
      }
    ]
  },
  {
    title: "Section B — Access & Identity Security",
    fields: [
      { key: "q6_mfa", label: "Is MFA enforced?", options: ANSWER_OPTIONS.yesNoRisk },
      { key: "q7_rbac", label: "Is RBAC implemented?", options: ANSWER_OPTIONS.yesNoRisk },
      { key: "q8_privileged_monitoring", label: "Are privileged accounts monitored and logged?", options: ANSWER_OPTIONS.yesNoRisk }
    ]
  },
  {
    title: "Section C — Data Protection",
    fields: [
      {
        key: "q9_encryption_at_rest",
        label: "Is data encrypted at rest?",
        options: [
          { label: "Yes", value: 1 },
          { label: "Unclear", value: 4 },
          { label: "No", value: 5 }
        ]
      },
      {
        key: "q10_encryption_in_transit",
        label: "Is data encrypted in transit?",
        options: [
          { label: "Yes", value: 1 },
          { label: "No", value: 5 }
        ]
      },
      {
        key: "q11_data_retention_policy",
        label: "Is there a defined data retention policy?",
        options: [
          { label: "Yes", value: 1 },
          { label: "No", value: 5 }
        ]
      }
    ]
  },
  {
    title: "Section D — Security Operations",
    fields: [
      { key: "q12_incident_response_plan", label: "Does the vendor have an incident response plan?", options: ANSWER_OPTIONS.yesNoRisk },
      {
        key: "q13_breach_notification_timeline",
        label: "Is there a defined breach notification timeline?",
        options: [
          { label: "Less than 72 hours", value: 1 },
          { label: "More than 72 hours", value: 3 },
          { label: "Not defined", value: 5 }
        ]
      },
      { key: "q14_log_monitoring", label: "Are logs monitored?", options: ANSWER_OPTIONS.yesNoRisk }
    ]
  },
  {
    title: "Section E — Compliance & Assurance",
    fields: [
      {
        key: "q15_certification",
        label: "Does the vendor have SOC 2 or ISO 27001 certification?",
        options: [
          { label: "Yes", value: 1 },
          { label: "In progress", value: 3 },
          { label: "No", value: 5 }
        ]
      },
      {
        key: "q16_security_audits",
        label: "Are regular security audits conducted?",
        options: [
          { label: "Yes", value: 1 },
          { label: "Occasionally", value: 3 },
          { label: "No", value: 5 }
        ]
      },
      { key: "q17_subprocessor_disclosure", label: "Are third-party subprocessors disclosed?", options: ANSWER_OPTIONS.yesNoRisk }
    ]
  },
  {
    title: "Section F — Resilience & Infrastructure",
    fields: [
      { key: "q18_bcdr", label: "Is there a business continuity and disaster recovery plan?", options: ANSWER_OPTIONS.yesNoRisk },
      { key: "q19_backups_tested", label: "Are backups performed and tested?", options: ANSWER_OPTIONS.yesNoRisk },
      {
        key: "q20_secure_hosting",
        label: "Is the hosting environment secure?",
        options: [
          { label: "Yes", value: 1 },
          { label: "Unclear", value: 3 },
          { label: "No", value: 5 }
        ]
      }
    ]
  }
];

export const evidenceFields = [
  "encryption_at_rest",
  "encryption_in_transit",
  "access_control",
  "incident_response",
  "logging_monitoring",
  "certification",
  "backups",
  "hosting_security"
] as const;

export const evidenceOptions = [
  { label: "Strong", value: "strong" },
  { label: "Medium", value: "medium" },
  { label: "Weak", value: "weak" },
  { label: "Missing", value: "missing" }
];
