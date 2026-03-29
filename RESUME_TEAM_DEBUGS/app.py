from flask import Flask, request, render_template, jsonify
import os
from src.resume_parser import parse_resume
from src.jd_parser import parse_job_description
from src.scorer import calculate_relevance_score
from src.llm_utils import get_llm_feedback

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    """Serves the main upload page."""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    API endpoint to analyze resume relevance.
    Receives resume and JD files, processes them, and returns results.
    """
    if 'resume' not in request.files or 'jd' not in request.files:
        return jsonify({"error": "Missing resume or job description file."}), 400

    resume_file = request.files['resume']
    jd_file = request.files['jd']

    try:
        # Step 1: Parse the files
        resume_text = parse_resume(resume_file)
        jd_data = parse_job_description(jd_file)

        # Step 2: Calculate relevance score
        score, missing_skills = calculate_relevance_score(resume_text, jd_data)

        # Step 3: Get personalized feedback from LLM
        feedback = get_llm_feedback(resume_text, jd_data)

        # Step 4: Determine verdict
        verdict = "High Suitability"
        if score < 60:
            verdict = "Low Suitability"
        elif score < 80:
            verdict = "Medium Suitability"

        return jsonify({
            "score": score,
            "verdict": verdict,
            "missing_skills": missing_skills,
            "feedback": feedback
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)