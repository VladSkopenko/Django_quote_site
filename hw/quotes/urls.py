from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path('register/', views.regis, name='register'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path("<int:page>", views.main, name="root_paginate"),
    #path("images/", views.pictures, name="pictures"),

]
