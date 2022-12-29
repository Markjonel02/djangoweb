from django import forms
from django.forms import ModelForm
from .models import Customers


class CutomersForm(ModelForm):
    
    class Meta:
        model = Customers
        fields = '__all__'#('Customersname','Customersnumber','Email','Address')

"""  widgets = {
            'Customersname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'Customersnumber': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ContactNumber'}),
            'Email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email.'}),
            'Address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
        } """