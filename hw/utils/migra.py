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

quotes = db.quotes.find()
for quote in quotes:
    tags = []
    for tag in quote["tags"]:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=quote["quote"])))

    if not exist_quote:
        author = db.authors.find_one({"_id": quote["author"]})
        aut = Author.objects.get(fullname=author["fullname"])
        quot = Quote.objects.create(quote=quote["quote"],
                                    author=aut,
                                    )
        for tag in tags:
            quot.tags.add(tag)

