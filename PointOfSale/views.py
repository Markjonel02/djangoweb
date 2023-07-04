from django.shortcuts import render,redirect
from ProductManagement.models import Product_crud
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.db.models import Q,Sum
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.


        

@login_required()
def search(request):
    
    if request.method == 'POST':
        search_item = request.POST.get('Searchitem_name')    
        request.session['search_results']= search_item  #stores sessions in the "search_results"  
    return JsonResponse({'success': search_item}, status=200)   


@login_required()
def pos(request):
    pos_prod = Product_crud.objects.all().order_by('Category')
    cart = CartQuantity.objects.all()
    form = CartQuantity_Form()
    if request.method =='POST':
        form = CartQuantity_Form(request.POST or None)
        if form.is_valid():
            prid = form.cleaned_data['product_id']
            form.save()
            prod  = Product_crud.objects.get(id=prid)
            
            price  = prod.Price
            quantity = int(form.cleaned_data["quantity"])
            total_price = price * quantity
            cartitem  = CartQuantity.objects.filter(product_id=prid)
            
            if cartitem.count() > 1: 
                print('you selected many')
                min = cartitem[0].id
                
                
                for carts in cartitem:
                    if carts.id < min:
                        min = carts.id
                
                base_cart = CartQuantity.objects.get(id=min)       
                if base_cart.quantity + quantity <=Product_crud.objects.get(id=base_cart.product_id).Current_Stock:
                    base_cart.quantity += quantity 
                    base_cart.total_price += total_price
                    base_cart.total_price += total_price
                    base_cart.save()
                else:
                    messages.error (request,'The desired quantity exceeds current Stock')
                for carts in cartitem:
                  if not carts.id == min:
                      carts.delete() 
            else:
                cartitem = CartQuantity.objects.get(product_id=prid)       
                total_price = quantity * price   
                itemname = prod.ItemName
                itemsize = prod.Sizes
                
                cartitem.total_price = total_price
                cartitem.name = itemname
                cartitem.size = itemsize
                cartitem.save()
            form = CartQuantity_Form()
                      
    context = {'pos_prod':pos_prod,'carts':cart,'form':form}
    return render(request,'POS/pos.html',context)    
            
       

   
