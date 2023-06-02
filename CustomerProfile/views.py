from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from .models import *
from CustomerProfile .forms import Customer_Form,Customers_FormUserChangeForm
from django.contrib import messages
# Create your views here.

#cutomers profile <--- start --->
#this will list an object created by the user and also can add
@login_required()
def customer_list(request):
    customers_crud = Customerprofile.objects.all()
    customers_crud  = Customerprofile.objects.order_by('-id')
    customers_form = Customer_Form()
    if request.method == 'POST':
        customers_form = Customer_Form(request.POST)
        if customers_form.is_valid():
            customers_form.save()
            messages.success(request,'New Customer has been Added ')
            customers_form = Customer_Form()
            return HttpResponseRedirect(reverse('customer_list'))
       
       
    return render(request, 'CustomerProfile/customersprofile.html', {'customers_form':customers_form,'customers_crud': customers_crud})
    customers_form = Customer_Form()  
    
        

   
def customer_edit(request,id):
    customeredit = get_object_or_404(Customerprofile,id=id)
    editform  = Customers_FormUserChangeForm(instance=customeredit)
    
    if request.method == 'POST':
        editform = Customers_FormUserChangeForm(request.POST or None, instance=customeredit)
        if editform.is_valid():
            editform.save()
            messages.success(request,'Customer '+ customeredit.customer_Lname +' info Successfully updated ')
            return HttpResponseRedirect(reverse('customer_list'))
            
    context = {
        'editform': editform,
        'customeredit':customeredit,
    }
         
    return render(request, 'CustomerProfile/edit _customer.html',context)
      
            
        
#delete funtion though its unecessary to have a delete in customer this will only based as understanding of how crud works
@login_required()
def del_customers(request,id):
    customers_crud = get_object_or_404(Customerprofile,id=id)
    if request.method == 'POST':
           customers_crud.delete()
           messages.warning(request,'Customer '+ customers_crud.customer_Lname +' successfully deleted' )
           return redirect('customer_list')
    context = {
        'customers_crud':customers_crud
    }
    return render(request,'CustomerProfile/delete.html',context)
