# app/summarizer.py

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Create client
client = genai.Client(api_key=API_KEY)


def summarize_transcript(transcript_text):
    if not API_KEY:
        return "Error: GEMINI_API_KEY not found in .env file"

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""... (same as before)"""
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating summary: {str(e)}"