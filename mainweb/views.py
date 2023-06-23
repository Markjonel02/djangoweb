from django.shortcuts import render, redirect, get_object_or_404
from .models import * 
from .forms import  * 
from django.contrib import messages
from django.views.generic import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from ProductManagement.models import Product_crud
from ProductManagement.views import products
from ProductManagement.forms import Product_crudForm
@login_required()
def dashboard(request):
  list_product=Product_crud.objects.all()
  return render(request, 'maintemp/dashboard.html',{'list_product':list_product})

   
#cutomers profile <--- End --->




# --- Uploading image on GuestPage---
# --- End of gallery --- 

#how to pass value from another modal in same page uisng jquery in django python?              

