

from django.views import View

from .forms import RegisterForm, LoginForm, ProfileForm
from .models import Profile

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib import messages


class RegisterView(View):
    template_name = "users/register.html"
    form_class = RegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="/")
        return super().dispatch(request, *args, **kwargs)

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
    profile_instance, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile_instance)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users:profile')

    profile_form = ProfileForm(instance=profile_instance)
    return render(request, 'users/profile.html', {'profile_form': profile_form})