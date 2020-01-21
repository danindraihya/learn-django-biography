from django.urls import path, include
from .views import (ListBiography, ListSearch, DetailBiography, CreateBiography, ManageBiography, DeleteBiography, UpdateBiography)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ListBiography.as_view(), name='index'),
    path('search/', ListSearch.as_view(), name='search'),
    path('detail/<str:slug>', DetailBiography.as_view(), name='detail'),
    path('create/', CreateBiography.as_view(), name='create'),
    path('manage/', ManageBiography.as_view(), name='manage'),
    path('delete/<int:pk>', DeleteBiography.as_view(), name='delete'),
    path('update/<int:pk>', UpdateBiography.as_view(), name='update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)