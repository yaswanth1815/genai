from groq import Groq
from dotenv import load_dotenv
import os

def query_rewriting(query):
    load_dotenv("api_keys.env")
    query_rew_key=os.getenv("query_rewriting_groq_api_key")
    Client=Groq(api_key=query_rew_key)


    prompt= f"""
    You are a query rewriting assistant.

    Rules:
    1. Rewrite the user query into ONLY ONE clear and optimized query.
    2. Do not generate multiple versions.
    3. Do not generate bullet points.
    4. Do not explain anything.
    5. Keep the rewritten query concise.
    6. Preserve the original meaning.
    7. Return only the rewritten query text.
    8.Preserve all entity names exactly
    9. Do not invent information
    10.Do not replace unknown words
    11.Fix only obvious grammar/spelling mistakes
    user query={query}
    """

    response=Client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role":"system",
                "content":(
                    '''You rewrite user queries
                        fro semantic retrieval systems
                    '''
                )
            },
            {
                "role":"user",
                "content":prompt
            }
        ],
        max_tokens=100,
        temperature=0,
        top_p=0.6
    )
    rewritten_query=(
        response.choices[0].message.content.strip()
    )

    return rewritten_query