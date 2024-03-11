from pymongo import MongoClient


def get_mongodb():
    client = MongoClient("mongodb+srv://vladgo:1111@goitlearn.x6ks5fo.mongodb.net/?retryWrites=true&w=majority")
    db = client.hw
    return db
