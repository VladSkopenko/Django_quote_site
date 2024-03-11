from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Author, Quote, Tag
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm, QuoteForm
from django.urls import reverse
from django.db import transaction


def main(request, page=1):
    quotes = Quote.objects.all().order_by('id')
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)

    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes/author_detail.html', {'author': author})


@login_required()
def add_author(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        born_date = request.POST.get('born_date')
        born_location = request.POST.get('born_location')
        description = request.POST.get('description')

        author = Author(
            fullname=fullname,
            born_date=born_date,
            born_location=born_location,
            description=description
        )
        author.save()

        return redirect(reverse('quotes:author_detail', args=[author.id]))

    return render(request, 'quotes/add_author.html')


@login_required()
def add_quote(request):
    if request.method == 'POST':
        quote_text = request.POST.get('quote_text')
        author_id = request.POST.get('author')
        tag_ids = request.POST.getlist('tags')

        author = get_object_or_404(Author, id=author_id)

        quote = Quote.objects.create(
            quote=quote_text,
            author=author,
        )

        tags = Tag.objects.filter(id__in=tag_ids)
        quote.tags.set(tags)

        return redirect('quotes:root')

    authors = Author.objects.all()
    tags = Tag.objects.all()
    return render(request, 'quotes/add_quote.html', {'authors': authors, "tags": tags})
