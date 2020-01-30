from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserProfileView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
    
urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', login_required(UserLogoutView.as_view()), name='logout'),
    path('profile/', login_required(UserProfileView.as_view()), name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)