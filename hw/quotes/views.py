from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from .models import Author
from .models import Quote
from .models import Tag


def get_top_10_tags():
    top_10_tags = Tag.objects.annotate(amount_quotes=Count("quote")).order_by("-amount_quotes")[:10]
    font_sizes = list(range(28, 9, -1))
    for i, tag in enumerate(top_10_tags):
        tag.font_size = font_sizes[i]
    return top_10_tags

def main(request, page=1):
    quotes = Quote.objects.all().order_by('id')
    top_10_tags = get_top_10_tags()
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)

    return render(request, "quotes/index.html", context={"quotes": quotes_on_page,
                                                         "top_tags": top_10_tags,
                                                         'paginator': paginator})


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



def show_quotes(request, tag_name, page=1):
    quotes = Quote.objects.filter(tags__name=tag_name)
    top_10_tags = get_top_10_tags()
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)

    return render(request, "quotes/index.html", context={"quotes": quotes_on_page,
                                                         "top_tags": top_10_tags,
                                                         'paginator': paginator})



