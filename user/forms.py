from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs = { 'class' : 'form-control' }))

    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]

        widgets = {
            'username' : forms.TextInput(
                attrs = {
                    'class' : 'form-control'
                }
            ),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'photo'
        ]

        widgets = {
            'photo' : forms.FileInput(
                attrs= {
                    'class' : 'form-control-file'
                }
            )
        }