from bson.objectid import ObjectId

from django import template

from ..utils import get_mongodb
from redis import StrictRedis
from redis_lru import RedisLRU

register = template.Library()
client = StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)

@cache
def get_author(id_):
    db = get_mongodb()
    author = db.authors.find_one({'_id': ObjectId(id_)})
    return author['fullname']


register.filter('author', get_author)
