# Risk Frontend Starter

A simple Next.js frontend starter for the AI-powered vendor risk assessment backend.

## Screens
- Dashboard
- New Assessment form
- Assessment results
- Risk register

## Setup

```bash
npm install
cp .env.local.example .env.local
npm run dev
```

Open `http://localhost:3000`

Make sure your backend is running and that `NEXT_PUBLIC_API_BASE_URL` points to it.

## Backend endpoint expected
- `POST /assessment/analyze`
