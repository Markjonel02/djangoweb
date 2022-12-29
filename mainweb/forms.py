from .models import Customers_crud
from django import forms
from django.forms import ModelForm

#Crud Form
class Customers_crudForm(ModelForm):
    
    class Meta:
        model = Customers_crud
        fields = '__all__'
        
        
        