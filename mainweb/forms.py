from .models import CreateNewList
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
class NewList(forms.ModelForm):
    email = forms.EmailField(required=True)
  
    class Meta:
        model = CreateNewList
        fields = ('name','contact','email','address')
        
        
        