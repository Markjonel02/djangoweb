from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def base(request):
    return render(request, 'guesttemp/base.html')
