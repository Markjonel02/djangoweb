from django.shortcuts import render, redirect,get_object_or_404
from .models import Customers # important add this line 
from .forms import CutomersForm# important add this line 
from django.urls import reverse_lazy
from django.views.generic import DeleteView
# Create your views here.

def listcustomer(request):
    customers = Customers.objects.all() #this means all the created object will list here  
    return render(request,'list.html',{'customers':customers})


# this will create the objects and pass to listcustomer
def createcustomer(request):
    form = CutomersForm()
    
    if request.method == 'POST':
        form = CutomersForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('customers_list')
    context={
        'form':form   
    }
    return render(request,'create.html',context)
        
        
        
def update(request, pk):
    customers = Customers.objects.get(id=pk)
    form = CutomersForm(instance=customers)

    if request.method == 'POST':
        form = CutomersForm(request.POST, instance=customers)
        if form.is_valid():
            form.save()
            return redirect('customers_list')

    context = {
        'form': form,
        'customers': customers,
    }
    return render(request, 'edit.html', context)
    
    
def deletecustomer(request, pk):
    customers = get_object_or_404(Customers, pk=pk)
    if request.method == 'POST':
        customers.delete()
        return redirect('customers_list')
     
    context= {
       
        'customers':customers,
    }
    return render(request, 'delete.html', context)
    
    
