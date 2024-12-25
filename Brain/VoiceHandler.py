import openai
from dotenv import load_dotenv
import os
import tempfile

# Load environment variables
load_dotenv()

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

def speech_to_text(audio_file):
    """Convert speech to text using OpenAI's Whisper model"""
    try:
        with open(audio_file, "rb") as audio:
            transcript = openai.audio.transcriptions.create(
                model="whisper-1",
                file=audio,
                response_format="text"
            )
        return transcript
    except Exception as e:
        print(f"Error in speech_to_text: {str(e)}")
        return None

def text_to_speech(text):
    """Convert text to speech using OpenAI's TTS model"""
    try:
        response = openai.audio.speech.create(
            model="tts-1",
            voice="nova",
            input=text
        )
        
        # Save to a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        response.stream_to_file(temp_file.name)
        return temp_file.name
    except Exception as e:
        print(f"Error in text_to_speech: {str(e)}")
        return None
