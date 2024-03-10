from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("quotes.urls")),
    path('users/', include('users.urls')),
    path('profile/', views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
