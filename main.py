from voice_processing import audio_input
from memory import store_chats
import uuid

session_id = str(uuid.uuid4())

def audio_query(audio_url):

    # import
    from voice_processing import audio_to_text

    # actual code
    text=audio_to_text.speech_to_text(audio_url)
    query_pipeline(text)

def query_pipeline(query):

    #imports 
    from mmai_query_related_methods import initial_processing
    from mmai_query_related_methods import query_rewriting,query_prompt_builder
    from models import llm_response
    from memory import previous_memory

    #actual code
    ini_proc_que=initial_processing.initial_processing(query)
    rewritten_query=query_rewriting.query_rewriting(ini_proc_que)
    final_query=query_prompt_builder.prompt_builder(rewritten_query)
    generated_answer=llm_response.llm_response(final_query)
    previous_memory.add_message("user",rewritten_query)
    previous_memory.add_message("assistant",generated_answer)
    return rewritten_query,generated_answer
    
def idp_pipeline(*url):

    from data_related_methods import(
        data_extract,
        data_chunks,
        custom_stopwords_removal, 
        data_lemmatisation,
        light_preprocessing,
        data_to_embeddings
    )
    from vector_db import pinecone_storage
    
    extracted_data=data_extract.extract_text(url)
    preprocessed_data=light_preprocessing.light_preprocessing(extracted_data)
    stopwords_remove=custom_stopwords_removal.custom_stopwords_removal(preprocessed_data)
    lemmatised_data=data_lemmatisation.data_lemmatise(stopwords_remove)
    chunks_created=data_chunks.chunk_data(lemmatised_data)
    embeddings=data_to_embeddings.data_to_embeddings(chunks_created)
    storage=pinecone_storage.vector_storing(embeddings,chunks_created)


print("Hey Hello whats Up!")
while(True):
    user_query=input("Enter Your Query (for audio query enter speech) (to exit enter exit)")

    if user_query.lower()=="exit":
        print("Session Closed")
        break
    if user_query.lower()=="speech":
        audio_input.record_audio()
        user_query=audio_query(r"data\audio_file.wav")

    rewritten_query,final_answer=query_pipeline(user_query)
    store_chats.store_chat(session_id,user_query,rewritten_query,final_answer)
    print(final_answer)
