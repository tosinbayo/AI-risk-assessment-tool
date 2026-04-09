# AI-Powered Vendor Risk Assessment Tool Starter

This is a FastAPI starter backend for an AI-assisted vendor risk assessment platform.

## What is included

- FastAPI API
- SQLAlchemy models
- Vendor assessment endpoint
- Deterministic scoring engine
- Risk finding rules
- Framework mappings
- File upload endpoint
- Evidence extraction stub for future AI integration
- PostgreSQL-ready configuration

## Project structure

```text
risk_backend_starter/
├── app/
│   ├── ai.py
│   ├── database.py
│   ├── main.py
│   ├── mappings.py
│   ├── models.py
│   ├── rules.py
│   ├── schemas.py
│   └── scoring.py
├── uploads/
├── .env.example
├── requirements.txt
└── README.md
```

## Quick start

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
cp .env.example .env
```

Then update `.env` with your actual values.

### 4. Start PostgreSQL

Create a database called `riskdb`.

### 5. Run the API

```bash
uvicorn app.main:app --reload
```

### 6. Open Swagger

```text
http://127.0.0.1:8000/docs
```

## Core endpoints

- `GET /` health message
- `POST /assessment/analyze` analyze a vendor assessment from questionnaire + evidence summary
- `POST /assessments/save` analyze and save an assessment to PostgreSQL
- `GET /assessments` list saved assessments
- `POST /files/upload` upload supporting evidence files
- `POST /files/extract-evidence` run a stub evidence extraction flow

## Notes

- The scoring engine is deterministic.
- The AI layer is intentionally a stub for grounded integration later.
- Final risk decisions should remain human-reviewed.
