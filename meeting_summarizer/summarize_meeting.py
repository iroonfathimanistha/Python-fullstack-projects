# summarize_meeting.py

from app.whisper_service import transcribe_audio
from app.summarizer import summarize_transcript
from app.utils import get_audio_file_path, save_transcript, save_text


def main():
    print("=== Meeting Summarizer (Day 4) ===\n")

    # 1. Get audio file
    try:
        audio_path = get_audio_file_path()
        print(f"✅ Audio found: {audio_path}")
    except FileNotFoundError as e:
        print(f"❌ {e}")
        return

    # 2. Transcribe
    print("\n🔄 Transcribing audio... (this may take a moment)")
    transcript = transcribe_audio(audio_path)
    if not transcript:
        print("❌ Transcription failed.")
        return

    # 3. Save raw transcript
    transcript_path = save_transcript(transcript, "raw_transcript.txt")
    print(f"📝 Raw transcript saved to {transcript_path}")

    # 4. Generate summary with Gemini
    print("\n🤖 Generating AI summary...")
    summary = summarize_transcript(transcript)

    # 5. Save summary
    summary_path = save_text(summary, "summaries/meeting_summary.md")
    print(f"📄 Summary saved to {summary_path}")

    # 6. Show preview
    print("\n--- Summary Preview ---")
    print(summary[:500] + "..." if len(summary) > 500 else summary)
    print("\n✅ Done!")


if __name__ == "__main__":
    main()