from django.contrib import admin
from django.urls import path, include
from .views import HomePage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='index'),
    path('biography/', include(('biography.urls', 'biography'), namespace='biography')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
