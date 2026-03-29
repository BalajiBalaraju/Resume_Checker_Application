# Resume Checker App

A smart web application designed to evaluate resumes against job descriptions and provide meaningful insights into candidate-job alignment. This tool helps users understand how well their resume matches a role and offers suggestions to improve their chances.

---

## Overview

Applying for jobs can be challenging, especially when you're unsure how well your resume fits a specific role. This application simplifies that process by analyzing both the resume and job description, then generating a compatibility score along with actionable feedback.

---

## Key Features

* Resume parsing and analysis
* Job description processing
* Intelligent scoring based on relevance
* AI-assisted insights for better evaluation
* Clean and simple web interface
* Dashboard view for results and feedback

---

## Project Structure

```
RESUME_TEAM_DEBUGS/
│
├── app.py                  # Entry point of the application
├── requirements.txt        # Project dependencies
├── README.md               # Documentation
│
├── src/
│   ├── resume_parser.py    # Extracts data from resumes
│   ├── jd_parser.py        # Processes job descriptions
│   ├── scorer.py           # Calculates match score
│   └── llm_utils.py        # Handles AI-related utilities
│
├── templates/
│   ├── index.html          # Home/upload page
│   └── dashboard.html      # Results display page
│
├── static/
│   ├── style.css           # Styling
│   └── script.js           # Client-side logic
```

---

## Setup Instructions

1. Clone the repository

```
git clone https://github.com/your-username/resume-checker.git
cd resume-checker
```

2. Create and activate a virtual environment

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install required dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```
python app.py
```

Then open your browser and navigate to:

```
http://127.0.0.1:5000/
```

---

## How It Works

1. The user uploads a resume and provides a job description
2. The system processes both inputs using parsing modules
3. Key skills, keywords, and relevant information are extracted
4. A scoring algorithm evaluates how well the resume matches the job
5. Results are displayed with insights and improvement suggestions

---

## Tech Stack

* Backend: Python (Flask)
* Frontend: HTML, CSS, JavaScript
* Processing: Custom parsing logic and AI utilities

---

## Future Enhancements

* Improved NLP-based keyword extraction
* Support for multiple file formats (PDF, DOCX)
* Enhanced scoring accuracy using advanced models
* Integration with job platforms and APIs

---

## Contribution

Contributions are always welcome. If you'd like to improve this project, feel free to fork the repository and submit a pull request.

---

## License

This project is open-source and available under the MIT License.
