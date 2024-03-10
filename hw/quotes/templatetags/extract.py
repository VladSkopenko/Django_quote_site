from bson.objectid import ObjectId
from quotes.models import Author

from django import template
#
# from ..utils import get_mongodb
from redis import StrictRedis
from redis_lru import RedisLRU

register = template.Library()
client = StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def get_author(author_id):
    try:
        author = Author.objects.get(pk=str(author_id))
        return author.fullname
    except Author.DoesNotExist:
        return "Unknown"


register.filter('author', get_author)
