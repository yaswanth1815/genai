import os
import uuid
from dotenv import load_dotenv
from pinecone import Pinecone,ServerlessSpec
session_id=str(uuid.uuid4())
def vector_storing(embeddings,chunks_created):
    load_dotenv("api_keys.env")
    pinecone_api=os.getenv("pinecone_api_key")
    pc=Pinecone(api_key=pinecone_api)
    index_name="idp-embeddings"
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )

        )
    index=pc.Index(index_name)
    vectors=[]
    i=0
    for embed in embeddings:
        vector={
            "id":f"ind-{i}",
            "values":embed.tolist(),
            "metadata":{
                "text":chunks_created[i],
                "chunk_id":i
            }
        }
        vectors.append(vector)
        i+=1
        index.upsert(vectors=vectors,namespace=session_id)
    
    return "Stored Successfully"


