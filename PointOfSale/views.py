from django.shortcuts import render,redirect
from ProductManagement.models import Product_crud
from django.contrib.auth.decorators import login_required
from .forms import CartQuantity_Form
from .models import *
from django.db.models import  Q
from django.http import JsonResponse
# Create your views here.


        

@login_required()
def search(request):
    
    if request.method == 'POST':
        search_item = request.POST.get('Searchitem_name')    
        request.session['search_results']= search_item  #stores sessions in the "search_results"  
    return JsonResponse({'success': search_item}, status=200)   


@login_required()
def pos(request):
    pos_prod=Product_crud.objects.all().order_by('Category')
    
    if 'search_results' in request.session:
        search_item = request.session['search_results']
        
        if search_item is not None:
            pos_prod = Product_crud.objects.filter(Q(ItemName__icontains=search_item) | Q(Category__icontains=search_item))
        else:
            pos_prod = Product_crud.objects.all().order_by('Category')
            request.session['search_results']=None
    else:
        pos_prod = Product_crud.objects.all().order_by('Category')
    
    return render(request, 'POS/pos.html',{'pos_prod':pos_prod})
     