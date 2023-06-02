from django.shortcuts import render,redirect,get_object_or_404  
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from .forms import Product_crudForm,product
from .models import Product_crud,pre_delete,product_archive
from django.contrib import messages
from django.db.models import Q

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
            messages.success(request, 'Successfull added a new a product')
            return redirect('product_list')
    
   
    return render(request,'Productmanagement/product_management.html',{'all_products':all_products,'archive':product_archive.objects.all(),'display_product':Product_crud.objects.all(),'display_product':Product_crud.objects.order_by('-id')})

# === Search  ===
def Search(request):
    query = request.GET.get('q')
    results = Product_crud.objects.filter(Q(search__icontains=query))
    return redirect('product_list')
# === Edit === 
@login_required()
def product_edit(request,id):
    list_product = Product_crud.objects.get(id=id)
    form = Product_crudForm(instance=list_product)
    #setting the username as readonly 
    form.fields['Max_Stock'].widget.attrs.update({'readonly':True})
    if request.method == 'POST':
        form = Product_crudForm(request.POST, instance=list_product)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    context = {
        'form': form,
        'list_product':list_product,
    }
    return render(request, 'Productmanagement/product_edit.html', context)
   
   
 #=== Add Stock ===  
def add_stock(request,id):
    list_products = get_object_or_404(Product_crud,id=id)
    form = product(instance=list_products)
    form.fields['Current_Stock'].widget.attrs.update({'readonly':True})
    if request.method =='POST':
        form = Product_crudForm(request.POST,instance=form)
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
           
     context = {
        'product_archive':product_archive,
       
    }
     return render(request,'Productmanagement/prod_del.html',context)
 
@login_required()
def archive(request):
    display = product_archive.objects.all()
    return render(request, 'Productmanagement/archive.html',{'display':display})
#product management<--- end --->
