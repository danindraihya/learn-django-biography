from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import CreateView
from django.core.signals import request_finished
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'user/index.html'
    success_url = reverse_lazy('user:login')

class UserLoginView(LoginView):
    template_name = 'user/login.html'

class UserLogoutView(LogoutView):
    template_name = 'user/logout.html'


class UserProfileView(TemplateView):
    user_form_class = UserUpdateForm
    profile_form_class = ProfileUpdateForm
    template_name = 'user/profile.html'

    def post(self, request):
        user_form = self.user_form_class(request.POST, instance=request.user)
        profile_form = self.profile_form_class(request.POST, request.FILES, instance=request.user.userprofile)

        context = self.get_context_data(user_form=user_form,
                                        profile_form=profile_form,
                                        )

        if user_form.is_valid():
            self.form_save(user_form)
        if profile_form.is_valid():
            self.form_save(profile_form)

            return self.render_to_response(context)

    def form_save(self, form):
        obj = form.save()
        return obj

    def get(self, request, *args, **kwargs):
        user_form = self.user_form_class(instance=request.user)
        profile_form = self.profile_form_class(instance=request.user.userprofile)

        context = self.get_context_data(user_form=user_form,
                                        profile_form=profile_form,
                                        )

        
        return self.render_to_response(context)
    
    