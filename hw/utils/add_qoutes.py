import json
from bson.objectid import ObjectId

from pymongo import MongoClient

client = MongoClient('mongodb+srv://vladgo:1111@goitlearn.x6ks5fo.mongodb.net')

db = client.hw

with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'tags': quote['tags'],
            'author': ObjectId(author['_id']),
            'quote': quote['quote']
        })
