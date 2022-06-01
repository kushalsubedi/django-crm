from django import forms
from .models import User, lead
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UsernameField

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model=lead
        fields =(
            'first_name',
            'last_name',
            'age',
            'agent',
        )


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name=forms.CharField()
    age= forms.IntegerField()


class CustomUserCreationForm(UserCreationForm):
    class Mets:
        model=User
        fields=('username',)
        field_classes = {'username': UsernameField}