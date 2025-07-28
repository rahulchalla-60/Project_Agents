import pdfplumber
# ✅ Correct
from langchain_google_genai import GoogleGenerativeAI


from langchain.prompts import PromptTemplate
from config import GEMINI_CONFIG, RESUME_PATH


def extract_resume_text(pdf_path=RESUME_PATH):
    """Extracts all text from the given PDF resume."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.strip()


def extract_skills_from_resume(text):
    """Extracts specific skills from resume text using Gemini via LangChain."""
    llm = GoogleGenerativeAI(
        model=GEMINI_CONFIG['model'],
        google_api_key=GEMINI_CONFIG['api_key']
    )
    prompt = PromptTemplate(
        input_variables=["resume_text"],
        template=(
            """
            You are a skills extractor. Given the following resume text, extract and return ONLY a list of technical skills, programming languages, frameworks, and tools mentioned in the resume. 
            
            Return the skills as a comma-separated list without any additional text or explanations.
            
            Examples of skills to extract: Python, JavaScript, React, Django, SQL, AWS, Git, etc.
            
            Resume:\n{resume_text}\n\nSkills:
            """
        )
    )
    chain = prompt | llm
    skills_response = chain.invoke({"resume_text": text})
    
    # Clean and split the skills
    skills_text = skills_response.strip()
    skills_list = [skill.strip() for skill in skills_text.split(',') if skill.strip()]
    return skills_list


if __name__ == "__main__":
    resume_text = extract_resume_text()
    print("\n--- Extracted Resume Text ---\n")
    print(resume_text[:1000] + ("..." if len(resume_text) > 1000 else ""))
    print("\n--- Extracted Skills ---\n")
    skills = extract_skills_from_resume(resume_text)
    print("Skills found:", skills) 