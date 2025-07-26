import whisper

from ..config import Config

def transcribe_audio(audio_path):
    """
    Converts audio file to text using Whisper.
    Returns the transcribed text or None if failed.
    """
    try:
        print("🔍 Loading Whisper model (may take a moment)...")
        model = whisper.load_model(Config.MODEL_SIZE)  # Uses 'base' by default
        
        print("🎤 Transcribing audio...")
        result = model.transcribe(audio_path)
        print("✅ Transcription successful!")
        return result["text"]
        
    except Exception as e:
        print(f"❌ Transcription failed: {e}")
        return None