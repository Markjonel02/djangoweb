from django import forms
from .models import CartQuantity
from django.forms import ModelForm,TextInput,HiddenInput,NumberInput
from ProductManagement.models import Product_crud
from django.core.exceptions import ValidationError

class CartQuantity_Form(forms.ModelForm):
    class Meta:
        model = CartQuantity
        fields = ('product_id','quantity')
        widgets = {'product_id': HiddenInput(),}
        
        def clean(self):
            cleaned_data = super().clean()
            qty = cleaned_data.get('quantity')
            prid = cleaned_data.get('product_id')
            product = Product_crud.objects.get(id=prid)
            
            if qty is not None:
                if qty > product.Current_Stock:
                    raise forms.ValidationError('Quantity cannot exceeds current stock!')
                if qty < 1:
                    raise forms.ValidationError('Quantity cannot be 0')