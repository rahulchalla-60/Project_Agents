import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_api_key():
    try:
        # Get API key from environment
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("No API key found in environment variables")
        
        genai.configure(api_key=api_key)
        
        # List available models
        print("🔍 Checking available models...")
        models = genai.list_models()
        
        print("✅ API Key is valid!")
        print("Available models:")
        for m in models:
            print(f"- {m.name}")
            
        # Test generation
        print("\n🧪 Testing model response...")
        model = genai.GenerativeModel('gemini-2.5-pro')
        response = model.generate_content("Say 'Hello World' in 3 languages")
        
        print("\nTest response:")
        print(response.text)
        
        return True
    except Exception as e:
        print("❌ API Key validation failed!")
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    test_api_key()