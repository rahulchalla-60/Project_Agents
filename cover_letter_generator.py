from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import GEMINI_CONFIG


def generate_cover_letter(resume_skills, job, resume_text=None):
    llm = GoogleGenerativeAI(
        model=GEMINI_CONFIG['model'],
        google_api_key=GEMINI_CONFIG['api_key']
    )

    prompt = PromptTemplate(
        input_variables=["skills", "job_title", "company", "location", "job_description", "resume_text"],
        template=(
            "Write a professional cover letter for the following job application.\n\n"
            "Job Title: {job_title}\n"
            "Company: {company}\n"
            "Location: {location}\n"
            "Job Description: {job_description}\n\n"
            "Applicant's Skills: {skills}\n"
            "{resume_text}\n\n"
            "The cover letter should be concise, highlight relevant skills and experience, and be tailored to the job and company.\n"
            "Start with a formal greeting, mention the job title and company, and explain why you are a great fit.\n"
            "End with a polite closing.\n\n"
            "Cover Letter:"
        )
    )

    skills_str = ", ".join(resume_skills)
    resume_text = resume_text or ""
    prompt_inputs = {
        "skills": skills_str,
        "job_title": job.get("title", ""),
        "company": job.get("company", ""),
        "location": job.get("location", ""),
        "job_description": job.get("description", ""),
        "resume_text": resume_text
    }

    # Use output parser to cleanly extract string
    chain = prompt | llm | StrOutputParser()
    try:
        response = chain.invoke(prompt_inputs)
        return response.strip()
    except Exception as e:
        return f"Error generating cover letter: {str(e)}"


if __name__ == "__main__":
    example_skills = ["Python", "Machine Learning", "Data Analysis", "Teamwork"]
    example_job = {
        "title": "Python Developer",
        "company": "Maxgen Technologies Private Limited",
        "location": "Ahmedabad",
        "description": "Work on Python backend systems, collaborate with a team, and develop scalable applications."
    }
    print("\n--- Generated Cover Letter ---\n")
    cover_letter = generate_cover_letter(example_skills, example_job)
    print(cover_letter)
