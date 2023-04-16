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
        
def clean_Customers(self):
        email = self.cleaned_data["CustomersEmail"]
        try:
            User.objects.get(CustomersEmail=CustomersEmail)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(_("A user with that email already exists."))        
class Product_crudForm(ModelForm):
    class Meta:
        model = Product_crud
        fields = '__all__'
        
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    
    #usermanagemnt 


class PhotoUPForm(forms.ModelForm):
   # categories =forms.CharField(label='Categories',widget=forms.Select(choices=pcategories)) 
    class Meta:
        model = PhotoUP
        fields = ('Itemname','Size','Category','Image')

# ====== Porcelain Form ======


# ====== End of Porcelain Form ======

