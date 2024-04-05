from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Count
from .models import Author, Quote, Tag


def main(request, page=1):
    quotes = Quote.objects.all().order_by('id')
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)

    return render(request, "quotes/index.html", context={"quotes": quotes_on_page, 'paginator': paginator})



def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes/author_detail.html', {'author': author})


def detail_tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    return render(request, "quotes/tag_detail.html", context={"tag": tag})


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


def search(request):
    if request.method == 'GET':
        tag = request.GET.get('tag', '')
        if tag:
            quotes = Quote.objects.filter(Q(tags__name__icontains=tag) | Q(author__fullname__icontains=tag))
        else:
            quotes = Quote.objects.all()
        return render(request, 'quotes/search_results.html', {'quotes': quotes})
    else:
        return render(request, 'quotes/search_results.html')


def quotes_by_tag(request, tag_id, page=1):
    tag = Tag.objects.get(pk=tag_id)
    quotes = Quote.objects.filter(tags=tag)

    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)

    # Запит до бази даних, щоб підрахувати кількість цитат для кожного тега
    top_tags = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]

    return render(request, 'quotes/quotes_by_tag.html',
                  {'tag': tag, 'quotes': quotes_on_page, 'paginator': paginator, 'top_tags': top_tags})
