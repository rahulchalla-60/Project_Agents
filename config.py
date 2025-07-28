from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_CONFIG = {
    'api_key': os.getenv("GEMINI_API_KEY"),
    'model': 'gemini-2.5-flash'  # Updated to working model
}

INTERNSHALA_CREDENTIALS = {
    'email': os.getenv("INTERNSHALA_EMAIL"),
    'password': os.getenv("INTERNSHALA_PASSWORD")
}

RESUME_PATH = "resume/Rahul_Challa_Resume.pdf"