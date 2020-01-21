from django import forms
from .models import Biography

class BiographyForm(forms.ModelForm):
    class Meta:
        model = Biography
        fields = [
            'title',
            'name',
            'gender',
            'place_of_birth',
            'date_of_birth',
            'description',
            'photo',
        ]

        widgets = {
            'gender' : forms.RadioSelect(
                attrs= {
                    'class' : 'form-check-input',
                }
            ),
            'date_of_birth' : forms.SelectDateWidget(
                attrs={
                    'class' : 'form-control col-sm-2 ml-1'
                }
            ),
        }