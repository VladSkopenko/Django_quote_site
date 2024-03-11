from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Author, Quote, Tag
from django.db.models import Count



def main(request, page=1):
    quotes = Quote.objects.select_related('author').prefetch_related('tags').all()
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)

    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes/author_detail.html', {'author': author})