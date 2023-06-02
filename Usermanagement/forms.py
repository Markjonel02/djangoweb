from  django import forms 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser
from django.forms import TextInput, HiddenInput, ModelForm, NumberInput, Select, DateInput, PasswordInput
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email','role',)
        widgets = {'first_name':TextInput(attrs={'class':'form-control'}),'last_name':TextInput(attrs={'class':'form-control'}),
                   'username':TextInput(attrs={'class':'form-control'}),'email':TextInput(attrs={'class':'form-control'}),
                   'role':Select(attrs={'class': 'role-select rounded p-2', 'required': 'required'})
            
        }
   
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email')
        widgets = {'first_name':TextInput(attrs={'class':'form-control'}),'last_name':TextInput(attrs={'class':'form-control'}),
                   'username':TextInput(attrs={'class':'form-control',}),'email':TextInput(attrs={'class':'form-control'}),
                   'role':Select(attrs={'class': 'role-select rounded p-2', 'required': 'required'})        
        }

    