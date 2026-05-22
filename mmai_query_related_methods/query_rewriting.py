from groq import Groq
from dotenv import load_dotenv
import os

def query_rewriting(query):
    load_dotenv("api_keys.env")
    query_rew_key=os.getenv("query_rewriting_groq_api_key")
    Client=Groq(api_key=query_rew_key)


    prompt= f"""
        You are a query rewriting system.

        Your task is to rewrite the user's query into ONE clear, concise, and retrieval-optimized query while strictly preserving the original meaning.

        Rules:

        1. Rewrite the query into ONLY ONE improved query.
        2. Never generate multiple versions.
        3. Never generate bullet points.
        4. Keep the rewritten query concise and natural.
        5. Preserve the original meaning exactly.
        6. Never answer the query.
        7. Never act like a chatbot or assistant.
        8. Never provide explanations or extra text.
        9. Preserve entity names, product names, IDs, and technical terms exactly.
        10. Do not invent information.
        11. Do not replace unknown words.
        12. Fix only obvious grammar and spelling mistakes.
        13. If the query is already clear and correct, return it unchanged.
        14. Preserve the user's tone and intent.
        15. For greetings, acknowledgements, gratitude, casual conversation, or short replies (example: "thanks", "okay", "nice", "cool", "thank you"), return the text unchanged.
        16. For follow-up conversational queries, rewrite them only enough to make the meaning clear while preserving context and intent.
        17. Return ONLY the rewritten query text.

    """

    response=Client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role":"system",
                "content":prompt
            },
            {
                "role":"user",
                "content":query
            }
        ],
        max_tokens=100,
        temperature=0,
        top_p=0.6,
        stream=False,
    )
    rewritten_query=(
        response.choices[0].message.content.strip()
    )

    return rewritten_query