from django import forms
from django.forms import ModelForm, TextInput, Select, NumberInput, FileInput, ModelChoiceField, IntegerField
from .models import Product_crud
from django.core.exceptions import ValidationError

class Product_crudForm(forms.ModelForm):
   
    class Meta:
        model = Product_crud
        fields = ('ItemName','Brand','Category','Sizes','Price','Current_Stock','Max_Stock','Status','Image')
        widgets  = {
            'ItemName':TextInput(attrs={'class':'form-control'}),'Brand':TextInput(attrs={'class':'form-control'}),
            'Sizes':Select(attrs={'class':'form-select'}),'Category':Select(attrs={'class':'form-select','required':'required'}),
            'Price':NumberInput(attrs={'class':'form-control'}),'Current_Stock':NumberInput(attrs={'class':'form-control'}),
            'Max_Stock':NumberInput(attrs={'class':'form-control'}),'Status':Select(attrs={'class':'form-select'}),'Image':FileInput(attrs={'class':'form-control'})
        }
        
    def clean(self):
      cleaned_data = super().clean()
      current_stock = cleaned_data['Current_Stock']
      max_stock = cleaned_data['Max_Stock']
      itemname = cleaned_data['ItemName']
      size = cleaned_data['Sizes']
 
       
      if Product_crud.objects.filter(ItemName=itemname).filter(Sizes=size).exists():
        raise forms.ValidationError("Product already exists")
      
      if max_stock < current_stock:
       raise forms.ValidationError('Max stocks cannot be less than current stock.')
class Product_EditForm(forms.ModelForm):
   
    class Meta:
        model = Product_crud
        fields = ('ItemName','Brand','Category','Sizes','Price','Current_Stock','Max_Stock','Status','Image')
        widgets  = {
            'ItemName':TextInput(attrs={'class':'form-control'}),'Brand':TextInput(attrs={'class':'form-control'}),
            'Sizes':Select(attrs={'class':'form-select'}),'Category':Select(attrs={'class':'form-select','required':'required'}),
            'Price':NumberInput(attrs={'class':'form-control'}),'Current_Stock':NumberInput(attrs={'class':'form-control'}),
            'Max_Stock':NumberInput(attrs={'class':'form-control'}),'Status':Select(attrs={'class':'form-select'}),'Image':FileInput(attrs={'class':'form-control'})
        }
     
class product(forms.ModelForm):
  class Meta:
    model = Product_crud
    fields = ('Current_Stock','Max_Stock')
    widgets  = {
      'Current_Stock':NumberInput(attrs={'class':'form-control'}),'Max_Stock':NumberInput(attrs={'class':'form-control'})
    }