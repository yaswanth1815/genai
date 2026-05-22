import os
from groq import Groq
from dotenv import load_dotenv

def speech_to_text(url):
    load_dotenv("api_keys.env")
    speech_api_key=os.getenv("whisper_model_api_key")
    client=Groq(api_key=speech_api_key)
    audio_file=open(url,"rb")
    converted_text=client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3-turbo",
            language="en",
            temperature=0,
            prompt="The following is an English conversation",
            response_format="verbose_json"
        )
    audio_file.close()
    return converted_text.text
