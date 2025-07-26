import sys
import os  # ← Keep this one (line 2)
from utils.youtube_handler import download_audio
from utils.transcription import transcribe_audio
from utils.notes_processor import process_text_to_notes, save_notes
from config import Config

def main():
    try:
        # Step 1: Get YouTube URL from user
        youtube_url = input("Enter YouTube video URL: ").strip()
        if not youtube_url:
            raise ValueError("❌ No URL provided")

        Config.YOUTUBE_URL = youtube_url

        # Step 2: Download audio
        print("\n⬇️ Downloading audio...")
        audio_path = download_audio(youtube_url)
        if not audio_path:
            raise RuntimeError("Failed to download audio")

        # Step 3: Transcribe audio to text
        print("\n🔊 Transcribing audio...")
        transcribed_text = transcribe_audio(audio_path)
        if not transcribed_text:
            raise RuntimeError("Failed to transcribe audio")

        # Step 4: Process text into notes
        print("\n✍️ Generating notes...")
        notes = process_text_to_notes(transcribed_text)
        if not notes:
            raise RuntimeError("Failed to process notes")

        # Step 5: Save notes
        output_path = os.path.join(Config.OUTPUT_DIR, "lecture_notes.txt")
        save_notes(notes, output_path)

        # Cleanup: Remove temporary audio file
        if os.path.exists(audio_path):
            os.remove(audio_path)

        print(f"\n🎉 Success! Notes saved to: {output_path}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("Please check the URL or try again.")

if __name__ == "__main__":
    main()