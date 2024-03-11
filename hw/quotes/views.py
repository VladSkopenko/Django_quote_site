from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Author, Quote, Tag
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm, QuoteForm
from django.urls import reverse
from django.db import transaction


def main(request, page=1):
    quotes = Quote.objects.select_related('author').prefetch_related('tags').all()
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


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            quote_text = form.cleaned_data['quote_text']
            tag_names = form.cleaned_data['tags']

            with transaction.atomic():
                quote = Quote.objects.create(
                    quote_text=quote_text,
                    author=author,
                    user=request.user
                )

                for tag_name in tag_names:
                    tag, _ = Tag.objects.get_or_create(name=tag_name)
                    quote.tags.add(tag)
                tag.save()
                quote.save()
            return redirect('quotes:root', author_id=author.id)
        else:
            return render(request, 'quotes/add_quote.html', {'form': form, 'authors': Author.objects.all()})

    authors = Author.objects.all()
    return render(request, 'quotes/add_quote.html', {'authors': authors})
