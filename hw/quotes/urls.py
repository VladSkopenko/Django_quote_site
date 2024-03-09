from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path('regis/', views.regis, name='regis'),
    path("<int:page>", views.main, name="root_paginate"),
    #path("images/", views.pictures, name="pictures"),

]
