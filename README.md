# Project Agents

A modular AI-powered agent that analyzes your resume, searches for matching jobs on Internshala, and generates tailored cover letters for each job using Google Gemini LLM.

---

## Features
- **Resume Analyzer:** Extracts text and skills from your PDF resume using Gemini LLM.
- **Job Searcher:** Scrapes Internshala for jobs matching your skills, with deduplication and fallback to mock data.
- **Cover Letter Generator:** Creates a professional, personalized cover letter for each job using Gemini LLM.
- **Orchestrator:** Runs the full workflow and prints results in a clear, step-by-step format.

---

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/rahulchalla-60/Project_Agents.git
cd Project_Agents
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
uv pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root with your Gemini API key and (optionally) Internshala credentials:
```
GEMINI_API_KEY=your_gemini_api_key_here
INTERNSHALA_EMAIL=your_email@example.com
INTERNSHALA_PASSWORD=your_password_here
```

### 5. Add Your Resume
Place your PDF resume in the `resume/` folder. Update the filename in `config.py` if needed.

---

## Usage

### Run the Full Agent Pipeline
```bash
python main.py
```

### What Happens:
1. **Resume Analyzer:** Extracts text and skills from your resume.
2. **Job Searcher:** Finds up to 5 unique jobs from Internshala matching your skills.
3. **Cover Letter Generator:** Generates a tailored cover letter for each job.
4. **Output:** Prints job details and cover letters to the console.

---

## Example Output
```
=== Resume Analyzer ===
Extracted resume text (first 500 chars):
...
Skills found: ['Python', 'Machine Learning', 'Data Analysis', ...]

=== Job Searcher ===

--- Job 1 ---
Title: Python Developer
Company: Maxgen Technologies Private Limited
Location: Ahmedabad
Description: Work on Python backend systems, collaborate with a team, and develop scalable applications.

Generating cover letter...

Cover Letter for Job 1:
Dear Hiring Manager, ...
============================================================
```

---

## Customization
- **Change number of jobs:** Edit `max_results` in `main.py`.
- **Change resume file:** Update `RESUME_PATH` in `config.py`.
- **Add more job sources:** Extend `job_searcher.py`.

---

## Dependencies
- Python 3.8+
- [uv](https://github.com/astral-sh/uv) (for fast dependency management)
- [langchain](https://python.langchain.com/)
- [langchain-google-genai](https://python.langchain.com/docs/integrations/llms/google_genai)
- [pdfplumber](https://github.com/jsvine/pdfplumber)
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

---

## License
MIT
