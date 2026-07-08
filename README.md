# Intrie

Intrie is an AI-powered interview preparation platform built with Python and Streamlit. It helps users prepare for job interviews by analyzing resumes, understanding job descriptions, generating skill assessments, simulating technical interviews, and providing actionable feedback and career guidance.

## Features

- Upload and analyze resumes in PDF or DOCX format
- Intake job descriptions, company details, and target roles
- Generate round-based skill assessments and interview questions
- Provide feedback, confidence scoring, and improvement roadmaps
- Recommend relevant companies and next-step career actions

## Tech Stack

- Python
- Streamlit
- Groq AI / LLM-based services
- PDF and DOCX parsing utilities

## Quick Start

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r intrie/requirements.txt
```

3. Set up your environment variables, including your Groq API key.
4. Run the app:

```bash
streamlit run intrie/app.py
```

## Notes

This project is designed to be modular and extensible, making it easy to enhance the AI interview experience over time.
