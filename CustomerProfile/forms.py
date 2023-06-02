from django.forms import TextInput, HiddenInput, ModelForm, NumberInput, Select, DateInput
from .models import Customerprofile
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
class Customer_Form(forms.ModelForm):
    class Meta:
        model = Customerprofile
        fields = '__all__'
        widgets = {'customer_Fname':TextInput(attrs={'class':'form-control'}),'customer_Middlename':TextInput(attrs={'class':'form-control'}),
                   'customer_Lname':TextInput(attrs={'class':'form-control'}),'sex':Select(attrs={'class': 'role-select rounded p-2', 'required': 'required'}),
                   'email':TextInput(attrs={'class':'form-control'}),'address':TextInput(attrs={'class':'form-control'}),
                   'contactnumber':NumberInput(attrs={'class':'form-control'})
            
        }
        
    def clean_email(self):
        #get all the variable 
        cleaned_data  = super().clean()
        email = cleaned_data['email']
        
     
        if Customerprofile.objects.filter(email=email).exists(): #check the email if existed if alredy exist raise validtion 
            raise forms.ValidationError('This email is already taken!')
        return email
      
            
            
class Customers_FormUserChangeForm(UserChangeForm):
    class Meta:
        model = Customerprofile
        fields = ('customer_Fname', 'customer_Middlename', 'customer_Lname','email', 'sex', 'address', 'contactnumber')
        widgets = {'customer_Fname':TextInput(attrs={'class':'form-control'}),'customer_Middlename':TextInput(attrs={'class':'form-control'}),
                   'customer_Lname':TextInput(attrs={'class':'form-control'}),'sex':Select(attrs={'class': 'role-select rounded p-2', 'required': 'required'}),
                   'email':TextInput(attrs={'class':'form-control'}),'address':TextInput(attrs={'class':'form-control'}),
                   'contactnumber':NumberInput(attrs={'class':'form-control'}),
            
        }