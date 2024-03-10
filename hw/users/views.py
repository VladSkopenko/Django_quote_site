from django.shortcuts import render, redirect

from django.views import View
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class RegisterView(View):
    template_name = "users/register.html"
    form_class = RegisterForm

    def get(self, request):
        return render(request, self.template_name, context={"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Hello {username}, Your account created successfully")
            return redirect(to="users:login")
        return render(request, self.template_name, context={"form": form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
