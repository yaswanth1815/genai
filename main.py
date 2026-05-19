from data_related_methods import data_extract,data_chunks
from data_related_methods import custom_stopwords_removal, data_lemmatisation
from data_related_methods import light_preprocessing, data_to_embeddings
from vector_db import pinecone_storage
from mmai_query_related_methods import initial_processing
from mmai_query_related_methods import query_rewriting,query_prompt_builder
from models import llm_response
from memory import previous_memory,store_chats
import uuid
session_id = str(uuid.uuid4())
def query_pipeline(query):
    ini_proc_que=initial_processing.initial_processing(query)
    rewritten_query=query_rewriting.query_rewriting(ini_proc_que)
    final_query=query_prompt_builder.prompt_builder(rewritten_query)
    generated_answer=llm_response.llm_response(final_query)
    previous_memory.add_message("user",rewritten_query)
    previous_memory.add_message("assistant",generated_answer)
    return rewritten_query,generated_answer
    
def idp_pipeline(*url):
    extracted_data=data_extract.extract_text(url)
    preprocessed_data=light_preprocessing.light_preprocessing(extracted_data)
    stopwords_remove=custom_stopwords_removal.custom_stopwords_removal(preprocessed_data)
    lemmatised_data=data_lemmatisation.data_lemmatise(stopwords_remove)
    chunks_created=data_chunks.chunk_data(lemmatised_data)
    embeddings=data_to_embeddings.data_to_embeddings(chunks_created)
    storage=pinecone_storage.vector_storing(embeddings,chunks_created)


print("Hey Hello whats Up!")
while(True):
    user_query=input("Enter Your Query (To exit type Exactly exit) ")
    if user_query.lower()=="exit":
        break
    rewritten_query,final_answer=query_pipeline(user_query)
    store_chats.store_chat(session_id,user_query,rewritten_query,final_answer)
    print(final_answer)
