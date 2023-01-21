from .models import *#Customers_crud, Product_crud, UserAdmin,PhotoUP
from django import forms
from django.forms import ModelForm
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
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
    
    
class PhotoUPForm(forms.ModelForm):
   # categories =forms.CharField(label='Categories',widget=forms.Select(choices=pcategories)) 
    class Meta:
        model = PhotoUP
        fields = ('Itemname','Size','Category','Image')

# ====== Porcelain Form ======
class PhotoUPporcelainForm(forms.ModelForm):
    
    class Meta:
        model = PhotoUPporcelain
        fields = ('Itemname_p','Size_p','Category_p','Image_p')

# ====== End of Porcelain Form ======


# ====== Ceramic ModelForm =======
class PhotoUPCeramicForm(forms.ModelForm):
    
    class Meta:
        model = PhotoUPCeramic
        fields = ('Itemname_c','Size_c','Category_c','Image_c')

# ====== Ceramic End ModelForm =======
        