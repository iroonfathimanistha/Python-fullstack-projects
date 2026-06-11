# process_audio_stub.py

from app.utils import get_audio_file_path, save_transcript


def main():
    print("=== Meeting Summarizer (Day 2 Stub) ===\n")

    # 1. Locate audio file
    try:
        audio_path = get_audio_file_path()
        print(f"✅ Audio file found: {audio_path}")
    except FileNotFoundError as e:
        print(f"❌ {e}")
        return

    # 2. Simulate transcription (will be replaced by Whisper on Day 3)
    dummy_transcript = """
Meeting Transcript (Simulated)
==============================

Attendees: John, Sarah, Mike

John: We need to finish the login page by Friday.
Sarah: I can help with the database design.
Mike: Let's schedule a follow-up on Monday.

Action items:
- John: Create login page
- Sarah: Design database schema
- Mike: Send calendar invite
"""

    # 3. Save the transcript
    transcript_path = save_transcript(dummy_transcript, "meeting_transcript.txt")
    print(f"\n📝 Transcript saved to: {transcript_path}")

    print("\n✅ Day 2 complete! Ready for Day 3.")


if __name__ == "__main__":
    main()