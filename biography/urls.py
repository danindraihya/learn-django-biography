from django.urls import path, include
from .views import (ListBiography, ListSearch)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ListBiography.as_view(), name='index'),
    path('search/', ListSearch.as_view(), name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)