import datetime
from connections.mongodb_connection import collection
def store_chat(session_id,user_query,rewritten_query,response):
    data={
        "session_id":session_id,
        "user_query":user_query,
        "rewritten_query":rewritten_query,
        "bot-response":response,
        "time":datetime.datetime.utcnow()
    }
    collection.insert_one(data)