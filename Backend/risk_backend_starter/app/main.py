import json
import os
import shutil
from pathlib import Path

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app import models
from app.ai import extract_text_preview, infer_evidence_from_text
from app.database import Base, engine, get_db
from app.rules import generate_findings, get_top_risk_flags
from app.schemas import (
    AssessmentInput,
    AssessmentOutput,
    ExtractEvidenceRequest,
    ExtractEvidenceResponse,
    FileUploadResponse,
    SavedAssessmentResponse,
    ScoreBreakdown,
)
from app.scoring import get_score_breakdown
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="AI-Powered Vendor Risk Assessment Tool",
    version="0.1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://vercel.com/oluwatosin-adebayos-projects/tools101.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
load_dotenv()
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")
Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI-Powered Vendor Risk Assessment Tool", version="0.2.0")


@app.get("/")
def root():
    return {"message": "Vendor Risk Assessment API is running"}


@app.post("/assessment/analyze", response_model=AssessmentOutput)
def analyze_assessment(payload: AssessmentInput):
    score_data = get_score_breakdown(payload.answers, payload.evidence)
    findings = generate_findings(payload.answers)
    top_risk_flags = get_top_risk_flags(payload.answers)

    return AssessmentOutput(
        vendor_name=payload.vendor_name,
        service_description=payload.service_description,
        score_breakdown=ScoreBreakdown(**score_data),
        findings=findings,
        top_risk_flags=top_risk_flags,
    )


@app.post("/assessments/save", response_model=SavedAssessmentResponse)
def save_assessment(payload: AssessmentInput, db: Session = Depends(get_db)):
    score_data = get_score_breakdown(payload.answers, payload.evidence)
    findings = generate_findings(payload.answers)
    top_risk_flags = get_top_risk_flags(payload.answers)

    vendor = db.query(models.Vendor).filter(models.Vendor.name == payload.vendor_name).first()
    if not vendor:
        vendor = models.Vendor(name=payload.vendor_name, description=payload.service_description)
        db.add(vendor)
        db.flush()

    assessment = models.Assessment(
        vendor_id=vendor.id,
        assessor_name=payload.assessor_name,
        service_description=payload.service_description,
        regulatory_scope=json.dumps(payload.regulatory_scope),
        inherent_risk_score=score_data["inherent_risk"],
        control_strength_score=score_data["control_strength"],
        evidence_confidence_score=score_data["evidence_confidence"],
        residual_risk_score=score_data["residual_risk"],
        risk_level=score_data["risk_level"],
        top_risk_flags=json.dumps(top_risk_flags),
        raw_answers_json=payload.answers.model_dump_json(),
        raw_evidence_json=payload.evidence.model_dump_json(),
    )
    db.add(assessment)
    db.flush()

    for finding in findings:
        db.add(models.Finding(
            assessment_id=assessment.id,
            title=finding.title,
            severity=finding.severity,
            description=finding.description,
            recommendation=finding.recommendation,
            framework_mapping=json.dumps(finding.framework_mapping),
        ))

    db.commit()
    db.refresh(assessment)

    return SavedAssessmentResponse(
        assessment_id=assessment.id,
        vendor_name=payload.vendor_name,
        service_description=payload.service_description,
        score_breakdown=ScoreBreakdown(**score_data),
        findings=findings,
        top_risk_flags=top_risk_flags,
    )


@app.get("/assessments")
def list_assessments(db: Session = Depends(get_db)):
    assessments = db.query(models.Assessment).order_by(models.Assessment.created_at.desc()).all()
    return [
        {
            "assessment_id": item.id,
            "vendor_id": item.vendor_id,
            "assessor_name": item.assessor_name,
            "service_description": item.service_description,
            "inherent_risk_score": item.inherent_risk_score,
            "control_strength_score": item.control_strength_score,
            "evidence_confidence_score": item.evidence_confidence_score,
            "residual_risk_score": item.residual_risk_score,
            "risk_level": item.risk_level,
            "created_at": item.created_at,
        }
        for item in assessments
    ]


@app.post("/files/upload", response_model=FileUploadResponse)
def upload_file(file: UploadFile = File(...)):
    destination = Path(UPLOAD_DIR) / file.filename
    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return FileUploadResponse(
        file_name=file.filename,
        content_type=file.content_type,
        saved_path=str(destination),
    )


@app.post("/files/extract-evidence", response_model=ExtractEvidenceResponse)
def extract_evidence(request: ExtractEvidenceRequest):
    if not Path(request.file_path).exists():
        raise HTTPException(status_code=404, detail="File not found")

    preview = extract_text_preview(request.file_path)
    evidence_summary, notes = infer_evidence_from_text(preview)

    return ExtractEvidenceResponse(
        file_path=request.file_path,
        extracted_text_preview=preview,
        evidence_summary=evidence_summary,
        notes=notes,
    )

