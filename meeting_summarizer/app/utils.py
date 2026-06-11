# app/utils.py

import os


def save_text(text, filename):
    """Save a string to a file. Creates directories if needed."""
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"✅ Saved to {filename}")


def get_audio_file_path(filename="meeting.wav", folder="uploads"):
    """
    Return the full path to an audio file.
    Optionally checks if the file exists.
    """
    path = os.path.join(folder, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Audio file not found: {path}")
    return path


def save_transcript(text, filename="transcript.txt", folder="transcripts"):
    """
    Save transcript text to the transcripts folder.
    Creates the folder if needed.
    """
    # Ensure folder exists
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Build full path
    filepath = os.path.join(folder, filename)

    # Save the text
    save_text(text, filepath)

    return filepath