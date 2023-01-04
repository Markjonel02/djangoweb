from django.shortcuts import render, redirect, get_object_or_404
from .models import Customers_crud
from .forms import Customers_crudForm
from django.views.generic import DeleteView

def dashboard(request):
    return render(request, 'maintemp/dashboard.html')


#cutomers profile <--- start --->
#this will list an object created by the user and also can add
def custom_list(request):
    customers_crud = Customers_crud.objects.all()
    
    if request.method == 'POST':
        form = Customers_crudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = Customers_crudForm()
    return render(request, 'maintemp/customersprofile.html', {'form': form, 'customers_crud': customers_crud})
   
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
def product_management(request):
    
    return render(request,'maintemp/productM/product_management.html')
#product management<--- end --->

 
           