import json
from mongoengine import Document, connect, StringField, ListField, ReferenceField

connect(db="hw", host=f"mongodb+srv://vladgo:1111@goitlearn.x6ks5fo.mongodb.net/?retryWrites=true&w=majority")


class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()
    meta = {
        'collection': 'authors'
    }


class Quote(Document):
    author = ReferenceField(Author)
    quote = StringField(required=True)
    tags = ListField(StringField())
    meta = {
        'collection': 'quotes'
    }


def load_quotes():
    with open("quotes.json", "r", encoding="utf-8") as file:
        data_quotes = json.load(file)
        for quote_data in data_quotes:
            author_name = quote_data.get('author')
            author = Author.objects.get(fullname=author_name) if author_name else None
            if author:
                quote = Quote(author=author,
                              tags=quote_data.get("tags"),
                              quote=quote_data.get("quote")
                              )
                quote.save()


load_quotes()
