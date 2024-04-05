from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")


def get_mongodb():
    client = MongoClient(mongo_uri)
    db = client.hw
    return db
