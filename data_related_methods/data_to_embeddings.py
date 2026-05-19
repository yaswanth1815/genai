from sentence_transformers import SentenceTransformer

def data_to_embeddings(text):
    model=SentenceTransformer("all-miniLM-L6-v2")
    embeds=model.encode(text)
    return embeds