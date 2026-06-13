# transcribe_meeting.py

from app.whisper_service import transcribe_audio
from app.utils import get_audio_file_path, save_transcript


def main():
    print("=== Meeting Transcriber (Real Whisper) ===\n")

    # 1. Get audio file
    try:
        audio_path = get_audio_file_path()
        print(f"✅ Audio found: {audio_path}")
    except FileNotFoundError as e:
        print(f"❌ {e}")
        return

    # 2. Transcribe
    transcript = transcribe_audio(audio_path)
    if not transcript:
        print("❌ Could not transcribe. Exiting.")
        return

    # 3. Save transcript
    output_file = "meeting_transcript.txt"
    saved = save_transcript(transcript, output_file)
    print(f"\n📄 Full transcript saved to: {saved}")

    # 4. Show statistics
    word_count = len(transcript.split())
    print(f"📊 Stats: {word_count} words, {len(transcript)} characters")


if __name__ == "__main__":
    main()