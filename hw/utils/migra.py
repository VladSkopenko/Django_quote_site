import os
import django

from pymongo import MongoClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw.settings")
django.setup()

from quotes.models import Quote, Tag, Author

# py -m utils.custom_migra

client = MongoClient('mongodb+srv://vladgo:1111@goitlearn.x6ks5fo.mongodb.net')

db = client.hw

authors = db.authors.find()
for author in authors:
    Author.objects.get_or_create(
        fullname=author.get("fullname"),
        born_date=author.get("born_date"),
        born_location=author.get("born_location"),
        description=author.get("description"),
    )
