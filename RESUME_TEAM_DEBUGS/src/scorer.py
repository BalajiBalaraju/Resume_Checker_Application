import random
from src.llm_utils import get_semantic_score

def calculate_relevance_score(resume_text, jd_data):
    """
    Calculates a relevance score for a resume against a job description.
    Combines hard-match and soft-match (semantic) scores.
    """
    # Simulate a hard-match score based on keywords.
    # In a full project, this would use TF-IDF, BM25, or fuzzy matching.
    hard_score = 0
    jd_skills = jd_data.get("required_skills", [])
    for skill in jd_skills:
        if skill.lower() in resume_text.lower():
            hard_score += 10
    
    # Simulate a semantic score using LLM.
    semantic_score = get_semantic_score(resume_text, jd_data)
    
    # Calculate weighted final score.
    final_score = (hard_score * 5) + (semantic_score * 5) + random.randint(10, 30)
    final_score = min(final_score, 100)
    
    # Simulate missing skills
    missing_skills = [
        "Cloud-native architecture", 
        "Data visualization with D3.js"
    ]

    return final_score, missing_skills