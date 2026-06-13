# app/action_items.py

import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)


def extract_action_items(transcript_or_summary):
    """
    Extract action items from a meeting transcript or summary.
    Returns a list of dictionaries.
    """
    if not API_KEY:
        return [{"error": "API key missing"}]

    try:
        prompt = f"""
You are a meeting assistant. Extract all action items from the following text.

Return ONLY a JSON array. Each item must have:
- "task": short description of the task
- "owner": person responsible (if mentioned, else "Unassigned")
- "deadline": if mentioned, else null

Example format:
[
  {{"task": "Create login page", "owner": "John", "deadline": "Friday"}},
  {{"task": "Design database", "owner": "Sarah", "deadline": null}}
]

If no action items, return [].

Text:
{transcript_or_summary}
"""
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=prompt
        )
        text = response.text.strip()
        # Remove markdown code blocks if present
        if text.startswith("```json"):
            text = text[7:]
        if text.endswith("```"):
            text = text[:-3]
        return json.loads(text)
    except Exception as e:
        return [{"error": f"Failed to parse: {str(e)}", "raw": response.text if 'response' in locals() else ""}]