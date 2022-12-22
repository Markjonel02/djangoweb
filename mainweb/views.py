from django.shortcuts import render, redirect 
from .models import CreateNewList
from .forms import NewList


def dashboard(request):
    return render(request, 'dashboard.html')

def custom(request):
    return render(request, 'customersprofile.html')

def Create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        address = request.POST.get('address')
        obj = NewList.objects.Create(name=name, contact=contact, email=email, address=address)
        obj.save()
        return redirect('customer')
         
   