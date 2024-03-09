from django.shortcuts import render

from django.views import View
from .forms import RegisterForm


class RegisterView(View):
    template_name = "users/register.html"
    form_class = RegisterForm

    def get(self, request):
        return render(request, self.template_name, context={"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()


