from django.shortcuts import render
from django.core.paginator import Paginator

from .utils import get_mongodb


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 5
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})


def regis(request):
    return render(request, "quotes/regis.html", context={})


def sign_up(request):
    if request.method == "POST":
        ...
    return render(request, "quotes/sign.html", context={})
