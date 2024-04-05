import json
import os

from bson.objectid import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)
db = client.hw

with open("quotes.json", "r", encoding="utf-8") as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({"fullname": quote["author"]})
    if author:
        db.quotes.insert_one(
            {
                "tags": quote["tags"],
                "author": ObjectId(author["_id"]),
                "quote": quote["quote"],
            }
        )
