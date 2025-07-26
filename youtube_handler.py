from pytube import YouTube, request
from pytube.exceptions import VideoUnavailable
import os
from config import Config

# Configure pytube request settings
request.default_range_size = 500000  # Smaller chunks for unstable connections
request.max_retries = 3  # Optional: adds retry attempts

def download_audio(youtube_url):
    """Downloads audio from YouTube video with enhanced error handling"""
    try:
        print("🔍 Fetching YouTube video...")
        
        # Create YouTube object (removed timeout parameter)
        yt = YouTube(
            youtube_url,
            use_oauth=False,
            allow_oauth_cache=True
        )
        
        # Check video availability
        yt.check_availability()
        
        # Get audio stream (fallback to any audio stream if filters fail)
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').last()
        if not audio_stream:
            audio_stream = yt.streams.get_audio_only()
            
        print(f"⬇️ Downloading: {yt.title}...")
        output_file = audio_stream.download(
            output_path=Config.OUTPUT_DIR,
            filename=Config.TEMP_AUDIO_FILE,
            skip_existing=False
        )
        print("✅ Audio downloaded successfully!")
        return output_file
        
    except VideoUnavailable:
        print("❌ Error: Video is unavailable or private")
    except Exception as e:
        print(f"❌ Error downloading audio: {str(e)}")
    return None