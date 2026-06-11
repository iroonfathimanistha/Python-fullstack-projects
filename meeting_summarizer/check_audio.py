# check_audio.py

import os

audio_file = "uploads/meeting.wav"

if os.path.exists(audio_file):
    print(f"✅ File found: {audio_file}")
    print(f"   File size: {os.path.getsize(audio_file)} bytes")
else:
    print(f"❌ File not found: {audio_file}")