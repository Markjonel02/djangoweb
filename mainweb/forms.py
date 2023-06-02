from .models import *#Customers_crud, Product_crud, UserAdmin,PhotoUP
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from django.forms import formset_factory # this allows you to manage multiple forms in one page 


#Crud Form
        
        
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    