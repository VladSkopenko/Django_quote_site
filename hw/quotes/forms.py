from django.forms import ModelForm, CharField, TextInput, Textarea
from .models import Author, Quote


class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=50, required=True, widget=TextInput())
    born_date = CharField(
        min_length=3, max_length=50, required=True, widget=TextInput()
    )
    born_location = CharField(
        min_length=3, max_length=150, required=True, widget=TextInput()
    )
    description = CharField(min_length=10, required=True, widget=Textarea())

    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description"]


class QuoteForm(ModelForm):
    quote = CharField(min_length=10, required=True, widget=Textarea())

    class Meta:
        model = Quote
        fields = ["quote", "tags", "author"]
