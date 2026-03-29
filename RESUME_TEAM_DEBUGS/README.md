Automated Resume Relevance Check System
An intelligent, AI-powered system designed to automate the tedious process of resume screening. This tool helps recruiters make faster, data-driven, and unbiased hiring decisions by scoring and analyzing resumes against job descriptions.

📽️ Demo
🎯 The Problem
In today's competitive job market, a single job posting can attract hundreds of resumes. Manually screening each one is:

Time-Consuming: Recruiters spend countless hours on repetitive filtering tasks.

Inconsistent: Evaluations can vary significantly between different recruiters.

Prone to Bias: Unconscious biases can lead to overlooking qualified candidates.

Lacks Feedback: Candidates, especially students, rarely receive constructive feedback to help them improve.

This project, developed for Innomatics Research Labs, aims to solve these challenges by leveraging the power of Generative AI.

✨ Features
AI-Powered Relevance Score: Generates a quantitative score (0-100) indicating how well a resume matches a job description.

Hybrid Analysis Engine: Combines traditional keyword matching (Hard Match) with contextual understanding (Semantic Match) for superior accuracy.

Gap Analysis: Clearly identifies key skills and qualifications from the job description that are missing in the resume.

Personalized AI Feedback: Provides actionable, constructive feedback for candidates to help them improve their resumes.

Interactive Web Dashboard: A clean, modern, and easy-to-use interface for uploading documents and viewing results.

Multi-Format Support: Accepts resumes and job descriptions in both PDF and DOCX formats.

⚙️ How It Works
The system follows a three-step workflow to provide a comprehensive analysis:

Data Ingestion: The user uploads a job description and a resume. The backend extracts clean text from these files using specialized parsers.

Relevance Analysis: The core AI engine processes the text.

The Hard Match module scans for direct keyword matches.

The Semantic Match module uses a Large Language Model (LLM) and a vector store to understand the contextual relevance between the two documents.

Output & Dashboard: The system combines the scores from both modules, generates a final verdict and personalized feedback, and displays everything on the user-friendly dashboard.

<p align="center">High-level system architecture</p>

🛠️ Technology Stack
Category	Technologies
Backend	🐍 Python, 🌐 Flask
AI & Data Processing	🤖 LangChain, 🧠 Google Gemini / OpenAI, PyMuPDF, python-docx
Vector Store	🗂️ ChromaDB
Frontend	📜 HTML, 🎨 CSS, ✨ JavaScript
Environment	📦 venv (Virtual Environment)

Export to Sheets
🚀 Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites
Python 3.10 or higher

An API key from an LLM provider (like Google AI Studio for Gemini or OpenAI)

⚙️ Installation & Setup
Clone the repository:

Bash

git clone https://github.com/your-username/automated-resume-checker.git
cd automated-resume-checker
Create and activate a virtual environment:

On Windows:

Bash

python -m venv venv
.\venv\Scripts\activate
On macOS/Linux:

Bash

python3 -m venv venv
source venv/bin/activate
Install the required dependencies:

Bash

pip install -r requirements.txt
Set up environment variables:



▶️ Running the Application
Set the Flask app environment variable:

On Windows:

Bash

set FLASK_APP=app.py
On macOS/Linux:

Bash

export FLASK_APP=app.py
Run the Flask development server:

Bash

flask run
Access the application:
Open your web browser and navigate to http://127.0.0.1:5000.

📂 Project Structure
/automated-resume-checker
├── app.py                  # Main Flask application file
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API keys)
├── src/
│   ├── resume_parser.py    # Extracts text from resumes
│   ├── jd_parser.py        # Extracts text from job descriptions
│   ├── scorer.py           # Core scoring logic
│   └── llm_utils.py        # Utilities for LLM interaction
├── static/
│   ├── style.css           # Frontend styles
│   ├── script.js           # Frontend logic
│   ├── demo.gif            # Demo GIF for README
│   └── architecture.png    # Architecture diagram
└── templates/
    └── index.html          # Main HTML page
🔮 Future Scope
ATS Integration: Integrate the system with popular Applicant Tracking Systems.

GitHub Profile Analysis: Add the ability to analyze a candidate's GitHub profile to validate their coding skills.

Batch Processing: Allow recruiters to upload multiple resumes at once for a single job description.

Advanced Analytics: Build a dashboard for the placement team to track skill gaps and trends across all student resumes.

🤝 Authors
This project was built by:

[AVINASH] - Project Lead

[BALAJI] - Technical Architect

[RAMU] - Product Demonstrator

A project for Innomatics Research Labs.
