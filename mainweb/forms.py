from .models import *#Customers_crud, Product_crud, UserAdmin,PhotoUP
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#Crud Form
class Customers_crudForm(ModelForm):    
    class Meta:
        model = Customers_crud
        fields = '__all__'
        
        
class Product_crudForm(ModelForm):
    class Meta:
        model = Product_crud
        fields = '__all__'
        
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    
    

class PhotoUPForm(forms.ModelForm):
   # categories =forms.CharField(label='Categories',widget=forms.Select(choices=pcategories)) 
    class Meta:
        model = PhotoUP
        fields = ('Itemname','Size','Description','Image','Category')
        
        