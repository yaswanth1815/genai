from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv("api_keys.env")
conn_string=os.getenv("mongodb_conn_string")
client=MongoClient(conn_string)
database=client['mmaidp_storage']
collection=database["chat_history"]