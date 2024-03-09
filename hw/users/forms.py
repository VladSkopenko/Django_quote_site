from django.forms import  CharField, ImageField, TextInput, FileInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class RegisterForm(UserCreationForm):
    username = CharField(max_length=19, min_length=2, required=True, widget=TextInput(attrs={"class": "form-control",}))


    class Meta:
        model = User
        fields = ["description", "path"]