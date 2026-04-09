import { AssessmentInput, AssessmentOutput } from "@/lib/types";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "http://127.0.0.1:8000";

export async function analyzeAssessment(payload: AssessmentInput): Promise<AssessmentOutput> {
  const response = await fetch(`${API_BASE_URL}/assessment/analyze`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload),
    cache: "no-store"
  });

  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || "Assessment request failed");
  }

  return response.json();
}
