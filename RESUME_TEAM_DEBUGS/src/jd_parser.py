# This is a placeholder file. In a real-world scenario, this would use a more
# advanced NLP library like spaCy or NLTK to extract entities and skills.
# It would also parse for must-have and good-to-have skills.

def parse_job_description(jd_file):
    """
    Parses a job description and extracts key data like skills and requirements.
    This is a simplified mock for demonstration.
    """
    jd_text = jd_file.read().decode('utf-8')
    
    # Mock data extraction based on keywords
    skills = ["Python", "Flask", "React", "Machine Learning", "NLP"]
    
    return {
        "text": jd_text,
        "required_skills": skills,
        "good_to_have_skills": []
    }