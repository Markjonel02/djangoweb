from django.shortcuts import render, redirect, get_object_or_404
from .models import Customers_crud, Product_crud,product_archive,PhotoUP
from .forms import Customers_crudForm, Product_crudForm,PhotoUPForm
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required()
def dashboard(request):
    return render(request, 'maintemp/dashboard.html')

#cutomers profile <--- start --->
#this will list an object created by the user and also can add
@login_required()
def custom_list(request):
    customers_crud = Customers_crud.objects.all()
    if request.method == 'POST':
        form = Customers_crudForm(request.POST)
        if form.is_valid():
            form.save()
            success_url = reverse_lazy('customer_list')
    else:
        form = Customers_crudForm()
    return render(request, 'maintemp/customersprofile.html', {'form': form, 'customers_crud': customers_crud})
   
"""  #search 
def search(request):
    form = SearchForm(request.GET)   
    if form.is_valid():
        query = form.cleaned_data['query']
        list_product = Product_crud.objects.filter()
        return render(request, 'maintemp/product_management.html', {'form': form, 'list_product':list_product})
    else:
        form = SearchForm()
        return render(request, 'maintemp/product_management.html', {'form':form}) """
   
   #end search form
   
   
   #edit function
def edit_customers(request,pk):
    customers_crud = Customers_crud.objects.get(id=pk)
    form = Customers_crudForm(instance=customers_crud)

    if request.method == 'POST':
        form = Customers_crudForm(request.POST, instance=customers_crud)
        if form.is_valid():
            form.save()
            return redirect('customer_list')

    context = {
        'form': form,
        'customers_crud': customers_crud,
    }
    return render(request, 'maintemp/crudmain/edit.html', context)
   
   
   #delet function
def del_customers(request,pk):
    customers_crud = get_object_or_404(Customers_crud,id=pk)
    if request.method == 'POST':
           customers_crud.delete()
           return redirect('customer_list')
    context = {
        'customers_crud':customers_crud
    }
    return render(request,'maintemp/crudmain/delete.html',context)

#cutomers profile <--- End --->

#product management<--- start --->
@login_required()
def product_list(request):
    list_product = Product_crud.objects.all()
    if request.method == 'POST':
        form = Product_crudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        
    form = Product_crudForm()
    
    context = {
        'list_product':list_product,
    }
    return render(request,'maintemp/product_management.html',context)

# === Edit === 

def product_edit(request,pk):
    list_product = Product_crud.objects.get(id=pk)
    form = Product_crudForm(instance=list_product)

    if request.method == 'POST':
        form = Product_crudForm(request.POST, instance=list_product)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    context = {
        'form': form,
        'list_product':list_product,
    }
    return render(request, 'maintemp/productM/product_edit.html', context)
   
#  === Archive ===
def product_del(request, pk):
     product_archive = get_object_or_404(Product_crud,id=pk)
 
     if request.method == 'POST':
           product_archive.delete()
           return redirect('product_list')
           
     context = {
        'product_archive':product_archive,
    }
     return render(request,'maintemp/productM/prod_del.html',context)
    
def archive(request):
    display =product_archive.objects.all()
    return render(request, 'maintemp/productM/archive.html',{'display':display})
#product management<--- end --->


 # --- Start usermanagement ---
def usermanagement(request):
       
    return render(request,'maintemp/usermanagement.html')

# --- End usermanagement ---           


# --- Uploading image on GuestPage---
def upload_image(request):
    if request.method == 'POST':
        form = PhotoUPForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dash')
    else:
        form = PhotoUPForm()
    return render(request, 'maintemp/uploadingGal.html', {'form': form})

      
# --- End of gallery --- 