from django.shortcuts import render

from django.views import View


class RegisterView(View):
    template_name = "users/register.html"
    def get(self):
        pass

    def post(self, request):
        pass
