from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Author, Quote, Tag
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm, QuoteForm


def main(request, page=1):
    quotes = Quote.objects.select_related('author').prefetch_related('tags').all()
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)

    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes/author_detail.html', {'author': author})


@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)

        if form.is_valid():
            author = form.save(commit=False)
            author.save()

            return redirect(to="quotes:author_detail", fullname=form.cleaned_data["author_id"])
        else:
            return render(
                request,
                "quotes/add_author.html",
                context={
                    "form": form,
                },
            )

    return render(
        request,
        "quotes/add_author.html",
        context={
            "form": AuthorForm(),
        },
    )
