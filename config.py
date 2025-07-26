import os

class Config:
    YOUTUBE_URL = ""
    OUTPUT_DIR = "outputs"
    TEMP_AUDIO_FILE = "temp_audio.mp4"
    MODEL_SIZE = "base"  # tiny, base, small, medium, large

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
