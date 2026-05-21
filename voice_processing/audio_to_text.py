import os
from groq import Groq
from dotenv import load_dotenv

def speech_to_text(url):
    load_dotenv("api_keys.env")
    speech_api_key=os.getenv("whisper_model_api_key")
    client=Groq(api_key=speech_api_key)

    with open(url,"rb") as audio_file:
        converted_text=client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3-turbo",
            temperature=0.2,
            response_format="verbose_json"
        )

    return converted_text.text
