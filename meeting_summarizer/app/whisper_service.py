import os
from faster_whisper import WhisperModel
def transcribe_audio(audio_path, model_size="base"):
    """
    Transcribe an audio file to text using Faster Whisper.
    """
    if not os.path.exists(audio_path):
        print(f"❌ Audio file not found: {audio_path}")
        return None

    try:
        print(f"🔄 Loading Whisper model '{model_size}'...")
        model = WhisperModel(model_size, device="cpu", compute_type="int8")

        print(f"🎤 Transcribing: {audio_path}")
        segments, info = model.transcribe(audio_path, beam_size=5)

        transcript = ""
        for segment in segments:
            transcript += segment.text + " "

        print(f"✅ Transcription complete. Detected language: {info.language}")
        return transcript.strip()

    except Exception as e:
        print(f"❌ Transcription error: {e}")
        print("   Possible fixes:")
        print("   - Check that FFmpeg is installed (ffmpeg -version)")
        print("   - Ensure the audio file is not corrupted")
        print("   - Try a shorter audio file (under 5 minutes)")
        return None