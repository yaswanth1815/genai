from groq import Groq


client = Groq(
    api_key="YOUR_GROQ_API_KEY"
)


def rewrite_query(query):

    prompt = f"""
You are an AI query rewriting assistant for a RAG system.

Your tasks:
1. Correct spelling mistakes
2. Correct grammar mistakes
3. Expand short queries into meaningful semantic search queries
4. Preserve original user intent
5. Make the query suitable for vector database retrieval
6. Return ONLY the rewritten query

User Query:
{query}
"""

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[

            {
                "role": "system",

                "content": (
                    "You rewrite user queries "
                    "for semantic retrieval systems."
                )
            },

            {
                "role": "user",

                "content": prompt
            }

        ],

        temperature=0,

        max_tokens=100
    )

    rewritten_query = (
        response
        .choices[0]
        .message
        .content
        .strip()
    )

    return rewritten_query


if __name__ == "__main__":

    query = "wher tajmahal locatd"

    rewritten_query = rewrite_query(query)

    print("\nOriginal Query:")
    print(query)

    print("\nRewritten Query:")
    print(rewritten_query)