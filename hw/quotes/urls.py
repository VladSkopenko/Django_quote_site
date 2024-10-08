from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('add_author/', views.add_author, name='add_author'),
    path("add_quote/", views.add_quote, name="add_quote"),
    path('search/', views.search, name='search'),
    path('quotes-by-tag/<int:tag_id>/', views.quotes_by_tag, name='quotes_by_tag'),
    path('quotes-by-tag/<int:tag_id>/<int:page>/', views.quotes_by_tag, name='quotes_by_tag_paginate'),
    path("tag/<str:tag_name>/", views.show_quotes, name="show_quotes"),
    path("tag/<str:tag_name>/page/<int:page>/", views.show_quotes, name="show_quotes_paginate"),
]


