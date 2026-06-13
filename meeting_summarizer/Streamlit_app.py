# streamlit_app.py (modified version)

import streamlit as st
import os
import tempfile
import json
from app.whisper_service import transcribe_audio
from app.summarizer import summarize_transcript
from app.action_items import extract_action_items
from app.utils import extract_audio_from_video, download_audio_from_url  # new imports

st.set_page_config(page_title="Meeting Summarizer", page_icon="🎙️")
st.title("🎙️ Automatic Meeting Summarizer")
st.markdown("Upload an audio/video file **or** paste a link (YouTube, etc.)")

# ----- Input Options -----
input_type = st.radio("Choose input method:", ["Upload File", "Paste URL"])

temp_path = None  # will hold the path to the audio file for transcription

if input_type == "Upload File":
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=["wav", "mp3", "m4a", "mp4", "mov", "avi", "mkv"],  # added video formats
        help="Audio: WAV, MP3, M4A; Video: MP4, MOV, AVI, MKV"
    )
    if uploaded_file is not None:
        # Display the file type
        st.audio(uploaded_file) if uploaded_file.type.startswith('audio') else st.video(uploaded_file)

        # Save uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            temp_path = tmp_file.name

        # If it's a video, extract audio
        if uploaded_file.type.startswith('video'):
            with st.spinner("Extracting audio from video..."):
                audio_path = extract_audio_from_video(temp_path)
                if audio_path:
                    temp_path = audio_path
                    st.success("Audio extracted successfully!")
                else:
                    st.error("Failed to extract audio from video.")
                    temp_path = None

elif input_type == "Paste URL":
    video_url = st.text_input("Enter video/audio URL (YouTube, Vimeo, etc.)")
    if video_url:
        with st.spinner("Downloading audio from link..."):
            temp_path = download_audio_from_url(video_url)
        if temp_path:
            st.success("Audio downloaded successfully!")
            # Optional: show video preview
            with st.expander("Preview"):
                st.video(video_url)
        else:
            st.error("Could not download audio from the provided link.")

# ----- Process Button -----
if temp_path and st.button("📝 Process Meeting", type="primary"):
    with st.spinner("🎤 Transcribing audio..."):
        transcript = transcribe_audio(temp_path)

    if not transcript:
        st.error("Transcription failed.")
    else:
        st.subheader("📝 Transcript")
        st.text_area("Full Transcript", transcript, height=200)

        with st.spinner("🤖 Generating summary..."):
            summary = summarize_transcript(transcript)
        st.subheader("📄 Summary")
        st.markdown(summary)

        with st.spinner("📋 Extracting action items..."):
            action_items = extract_action_items(summary)
        st.subheader("✅ Action Items")
        if isinstance(action_items, list) and action_items:
            for idx, item in enumerate(action_items, 1):
                st.markdown(f"**{idx}. {item.get('owner', 'Unassigned')}**: {item.get('task', '')}")
        else:
            st.info("No action items found.")

        col1, col2 = st.columns(2)
        with col1:
            st.download_button("Download Summary", summary, file_name="summary.md")
        with col2:
            st.download_button("Download Action Items", json.dumps(action_items), file_name="action_items.json")

# Cleanup (optional): delete temporary files after use
if temp_path and os.path.exists(temp_path):
    os.unlink(temp_path)