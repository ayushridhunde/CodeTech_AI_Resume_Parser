import pdfplumber
import re

def extract_details(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + " "
    except Exception as e:
        print(f"Error reading PDF: {e}")

    # Email extraction
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    email = email_match.group(0) if email_match else "Not Found"

    # Skills extraction (Simple logic)
    skill_set = ['Python', 'Flask', 'SQL', 'PostgreSQL', 'Machine Learning', 'Java', 'HTML', 'CSS', 'React', 'C++', 'Data Science']
    found_skills = [skill for skill in skill_set if skill.lower() in text.lower()]

    return {
        "email": email,
        "skills": ", ".join(found_skills) if found_skills else "No skills found"
    }