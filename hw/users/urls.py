from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = "users"

urlpatterns = [
    path("signup/", views.main, name="signup"),
    path("signin/", LoginView.as_view(), name="signin"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
