from django.shortcuts import render,redirect
from ProductManagement.models import Product_crud

# Create your views here.
def pos(request):
    
    return render(request, 'POS/pos.html')

def porcelain_up(request):
     pos_p = Product_crud.objects.filter(Category='porcelain')
     return render(request, 'POS/porcelain.html',{'pos_p':pos_p})