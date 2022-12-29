from django.shortcuts import render, redirect 
from .models import Customers_crud
from .forms import Customers_crudForm


def dashboard(request):
    return render(request, 'dashboard.html')

def custom_list(request):
    customers_crud = Customers_crud.objects.all()
    context = {
        'customers_crud':customers_crud
    }
    return render(request, 'customersprofile.html',context)

#creating list and pass it to customers list 
def create_list(request):
    form = Customers_crudForm()
    
    if request.method == 'POST':
        form = Customers_crudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
        
        context = {
            'form':form
        }
        return render(request, 'create_crud.html',context)
    