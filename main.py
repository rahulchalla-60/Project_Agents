from resume_analyzer import extract_resume_text, extract_skills_from_resume
from job_searcher import search_jobs
from cover_letter_generator import generate_cover_letter
from config import RESUME_PATH


def main():
    print("\n=== Resume Analyzer ===\n")
    resume_text = extract_resume_text(RESUME_PATH)
    print(f"Extracted resume text (first 500 chars):\n{resume_text[:500]}\n{'...' if len(resume_text) > 500 else ''}")

    print("\nExtracting skills from resume...\n")
    skills = extract_skills_from_resume(resume_text)
    print(f"Skills found: {skills}\n")

    print("\n=== Job Searcher ===\n")
    jobs = search_jobs(skills, max_results=5)
    if not jobs:
        print("No jobs found.")
        return
    for idx, job in enumerate(jobs, 1):
        print(f"\n--- Job {idx} ---")
        print(f"Title: {job['title']}")
        print(f"Company: {job['company']}")
        print(f"Location: {job['location']}")
        print(f"Description: {job['description']}")

        print("\nGenerating cover letter...")
        cover_letter = generate_cover_letter(skills, job, resume_text=resume_text)
        print(f"\nCover Letter for Job {idx}:\n{cover_letter}")
        print("\n" + "="*60)

if __name__ == "__main__":
    main() 