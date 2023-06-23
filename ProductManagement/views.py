from django.shortcuts import render,redirect,get_object_or_404  
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from .forms import *
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
# Create your views here.
    #product.fields['ItemName'].widget.attrs.update({'class':'form-control'}) #setting the username as readonly 

#product management<--- start --->
@login_required()
def products(request):
    all_products = Product_crudForm()
    if request.method == 'POST':
        all_products = Product_crudForm(request.POST, request.FILES)
        if all_products.is_valid():
            all_products.save()
            messages.success(request, 'New product has been added')
            return redirect('product_list')
            all_products = Product_EditForm()
    return render(request,'Productmanagement/product_management.html',{'all_products':all_products,'archive':product_archive.objects.all(),'display_product':Product_crud.objects.all(),'display_product':Product_crud.objects.order_by('-id')})

# === Search  ===
      
  
# === Edit === 
@login_required()
def product_edit(request,id):
    list_product = Product_crud.objects.get(id=id)
    form = Product_EditForm(instance=list_product)
    #setting the username as readonly 
    form.fields['Max_Stock'].widget.attrs.update({'readonly':True})
    if request.method == 'POST':
        form = Product_EditForm(request.POST, instance=list_product)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    context = {
        'form': form,
        'list_product':list_product,
    }
    return render(request, 'Productmanagement/product_edit.html', context)
   
   
 #=== Add Stock ===  
login_required()
def add_stock(request,id):
    list_products = get_object_or_404(Product_crud,id=id)
    form = product(instance=list_products)
    form.fields['Current_Stock'].widget.attrs.update({'readonly':True})
    if request.method =='POST':
        form = product(request.POST, instance=list_products)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sucessfully added to stock')
            return redirect('product_list')
        
            
    return render(request, 'Productmanagement/add_stock.html',{'form':form})



   
#  === Archive ===
@login_required()
def product_del(request, id):
     product_archive = get_object_or_404(Product_crud,id=id)
     if request.method == 'POST':
           product_archive.delete()
           return redirect('product_list')
           messages.warning(request,'one record deleted!')
       
           
     context = {
        'product_archive':product_archive,
       
    }
     return render(request,'Productmanagement/prod_del.html',context)
 
@login_required()
def archive(request):
    display = product_archive.objects.all()
    return render(request, 'Productmanagement/archive.html',{'display':display})
#product management<--- end --->
    