from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def base(request):
    return render(request, 'guesttemp/base.html')
""" 
def register(request):
    if request.method  == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'new account created:{username}')
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
        else:
            messages.error(request,"account creation failed")
            
            return redirect("base")
        form = UserCreationForm()
        return render(request, 'register.html',{'form':form})
         """


