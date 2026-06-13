# Add these functions to your existing app/utils.py

import subprocess
import yt_dlp
import tempfile
import os


def extract_audio_from_video(video_path, output_format="wav"):
    """
    Extract audio from a video file (MP4, MOV, AVI, etc.) using ffmpeg.
    Returns path to temporary audio file.
    """
    try:
        # Create a temporary file for the audio
        temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=f".{output_format}")
        temp_audio.close()

        # Use ffmpeg to extract audio
        # -i input file -vn (no video) -acodec pcm_s16le (WAV format) -ar 16000 (sample rate)
        cmd = [
            "ffmpeg", "-i", video_path, "-vn",
            "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1",
            temp_audio.name, "-y"  # -y overwrite output if exists
        ]
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        return temp_audio.name
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg error: {e.stderr}")
        return None
    except Exception as e:
        print(f"Error extracting audio: {e}")
        return None


def download_audio_from_url(url):
    """
    Download audio from a video sharing URL (YouTube, etc.) and return path to temporary audio file.
    """
    try:
        # Create temporary file name (without extension, yt-dlp will add .mp3)
        temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        temp_path = temp_audio.name
        temp_audio.close()

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': temp_path.replace('.mp3', ''),  # remove extension; yt-dlp adds it
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # yt-dlp may have added .mp3 extension
        if os.path.exists(temp_path):
            return temp_path
        elif os.path.exists(temp_path + ".mp3"):
            return temp_path + ".mp3"
        else:
            return None
    except Exception as e:
        print(f"Download error: {e}")
        return None