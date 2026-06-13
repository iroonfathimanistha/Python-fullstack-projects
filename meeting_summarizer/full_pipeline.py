# full_pipeline.py

from app.whisper_service import transcribe_audio
from app.summarizer import summarize_transcript
from app.action_items import extract_action_items
from app.utils import get_audio_file_path, save_transcript, save_text
import json


def main():
    print("=== Full Meeting Summarizer (Day 5) ===\n")

    # 1. Get audio file
    try:
        audio_path = get_audio_file_path()
        print(f"✅ Audio found: {audio_path}")
    except FileNotFoundError as e:
        print(f"❌ {e}")
        return

    # 2. Transcribe
    print("\n🔄 Transcribing audio...")
    transcript = transcribe_audio(audio_path)
    if not transcript:
        print("❌ Transcription failed.")
        return
    save_transcript(transcript, "transcripts/raw_transcript.txt")

    # 3. Generate summary
    print("\n🤖 Generating summary...")
    summary = summarize_transcript(transcript)
    save_text(summary, "summaries/meeting_summary.md")

    # 4. Extract action items from the summary (or use transcript)
    print("\n📋 Extracting action items...")
    action_items = extract_action_items(summary)  # you can also use transcript

    # 5. Save action items as JSON
    with open("summaries/action_items.json", "w", encoding="utf-8") as f:
        json.dump(action_items, f, indent=2)

    # 6. Save action items as readable markdown
    md_content = "# Action Items\n\n"
    for item in action_items:
        task = item.get("task", "Unknown task")
        owner = item.get("owner", "Unassigned")
        deadline = item.get("deadline", "")
        line = f"- **{owner}**: {task}"
        if deadline:
            line += f" (by {deadline})"
        md_content += line + "\n"

    save_text(md_content, "summaries/action_items.md")

    print("\n✅ Results saved:")
    print("   - Summary: summaries/meeting_summary.md")
    print("   - Action items (JSON): summaries/action_items.json")
    print("   - Action items (Markdown): summaries/action_items.md")


if __name__ == "__main__":
    main()