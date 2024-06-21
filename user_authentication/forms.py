# forms.py
from django import forms
from .models import Signup
from django.forms import ModelForm


class SignupForm(ModelForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = Signup
        fields = '__all__'




