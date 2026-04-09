
from pathlib import Path

def extract_text_preview(file_path: str, max_chars: int = 1200) -> str:
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read(max_chars)
    except Exception:
        return "Unable to extract text preview"


def infer_evidence_from_text(text: str):
    # placeholder logic
    return {
        "confidence": 0.5,
        "category": "unknown",
        "notes": "basic inference placeholder"
    }
