# Intrie

Intrie is a Streamlit-based AI interview preparation workspace that analyzes a user's resume and job description, simulates interview rounds, and generates actionable feedback.

## Features

- Resume upload for PDF and DOCX files
- Job description, company, and role intake
- Round 1 skill assessment planning and scoring
- Round 2 conversational technical interview flow
- Confidence score, roadmap, and company recommendations
- Modular codebase ready for deeper Groq-driven AI flows

## Quick Start

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and add your Groq API key.
4. Run the app:

```bash
streamlit run app.py
```

## Project Notes

- The app uses environment variables for secrets and runtime configuration.
- Service modules are intentionally separated from UI modules to keep the codebase scalable.
- If the Groq API key is missing, the app falls back to deterministic mock responses so the UI remains usable during setup.
