from .models import *#Customers_crud, Product_crud, UserAdmin,PhotoUP
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from django.forms import formset_factory # this allows you to manage multiple forms in one page 


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
    
    #usermanagemnt 


class PhotoUPForm(forms.ModelForm):
    class Meta:
        model = PhotoUP
        fields = ('Itemname','Size','Category','Image')


# -- usermanagement -- 
class CustomUserManagementForm(ModelForm):
    class Meta:
        model = UserManagement()
        fields = ('email','user_name','first_name','is_staff','is_active')
       
