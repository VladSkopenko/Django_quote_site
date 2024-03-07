from django.shortcuts import render


def main(request):
    return render(request, "quotes/index.html", context={})
