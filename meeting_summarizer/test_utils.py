# test_utils_day2.py

from app.utils import get_audio_file_path, save_transcript

# Test 1: Get audio file path
try:
    audio_path = get_audio_file_path()
    print(f"Audio path: {audio_path}")
except FileNotFoundError as e:
    print(f"Error: {e}")

# Test 2: Save a dummy transcript
dummy_text = "This is a test transcript from Day 2."
saved_path = save_transcript(dummy_text, "dummy.txt")
print(f"Transcript saved to: {saved_path}")