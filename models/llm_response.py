from groq import Groq
from dotenv import load_dotenv
import os


def llm_response(messages):
    load_dotenv("api_keys.env")
    api_key=os.getenv("llm_api_key")
    client=Groq(api_key=api_key)

    response=client.chat.completions.create(
        model="openai/gpt-oss-120b",
        temperature=0.4,
        top_p=0.6,
        reasoning_effort="medium",
        messages=messages,
        stream=True
    )

    full_responce=""
    for chunk in response:
        data=chunk.choices[0].delta.content
        if data:
            full_responce+=data

    return full_responce
    
