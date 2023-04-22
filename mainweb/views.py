from django.shortcuts import render, redirect, get_object_or_404
from .models import * 
from .forms import  * 
from django.contrib import messages
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

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
    
    return render(request, 'maintemp/customersprofile.html', {'form':form, 'customers_crud': customers_crud})
   

   
   
   #edit function
@login_required()
def edit_customers(request):
    
    if request.method == 'POST':
        #this will get the value 
    
     customers_edit = get_object_or_404(Customers_crud, pk=request.POST["editpk"])
     customers_edit.CustomersName = request.POST['CustomersName']
     customers_edit.ContactNumber = request.POST['ContactNumber']
     customers_edit.CustomersEmail = request.POST['CustomersEmail']
     customers_edit.CustomerAdd = request.POST['CustomersAdd']
     customers_edit.save()
     messages.info(request, 'update successfuly!')
     
    elif request.method == 'POST':
     customers_edit.CustomersName = request.POST['']
     customers_edit.ContactNumber = request.POST['']
     customers_edit.CustomersEmail = request.POST['']
     customers_edit.CustomerAdd = request.POST['']
     return redirect('customer_list')

   #delet function
@login_required()
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
        'display':product_archive.objects.all()
    }
    return render(request,'maintemp/product_management.html',context)

# === Edit === 
@login_required()
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
@login_required()
def product_del(request, pk):
     product_archive = get_object_or_404(Product_crud,id=pk)
 
     if request.method == 'POST':
           product_archive.delete()
           return redirect('product_list')
           
     context = {
        'product_archive':product_archive,
       
    }
     return render(request,'maintemp/productM/prod_del.html',context)
 
@login_required()
def archive(request):
    display =product_archive.objects.all()
    return render(request, 'maintemp/productM/archive.html',{'display':display})
#product management<--- end --->


 # --- Start usermanagement ---
@login_required()
def usermanagement(request):
   
        return render(request,'maintemp/usermanagement.html')
# --- End usermanagement ---           


# --- Uploading image on GuestPage---
@login_required()
def adupload_image(request):
 
    #  ==== adhesive submit form =====
    if request.method == 'POST':
        form = PhotoUPForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('upload')  #return to dash after    
    else:        
        form = PhotoUPForm()    
        # *****  porcelain submit form ******

    if request.method == 'POST':
        formporcelain = PhotoUP(request.POST, request.FILES)
        if formporcelain.is_valid():
            formporcelain.save()
            return redirect('upload')  #return to dash after    
    else:        
        formporcelain = PhotoUPForm()
        

            
        
        
        return render(request, 'maintemp/uploadingGal.html',{
         'formporcelain':formporcelain,
         'form':form
       }) 



# --- End of gallery --- 

#how to pass value from another modal in same page uisng jquery in django python?              

