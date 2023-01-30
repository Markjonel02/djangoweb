from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
#from mainweb.views import *
from mainweb.models import *#PhotoUP, PhotoUPporcelain



# Create your views here.
def base(request):
    return render(request,'guesttemp/base.html')  

#def all(request):
    #return render(request,'guesttemp/All.html',)


def guest_up(request):
    #if request.method == 'GET':     
     posts = PhotoUP.objects.all()
     return render(request, 'guesttemp/Adhesive.html',{'posts':posts})

def porcelain_up(request):
     pos_p = PhotoUPporcelain.objects.all()
     return render(request, 'guesttemp/Porcelaintile.html',{'pos_p':pos_p}) 

def ceramic_up(request):
     cer_p  = PhotoUPCeramic.objects.all()
     return render(request, 'guesttemp/Ceramictile.html',{'cer_p':cer_p}) 
 
 
def skim_up(request):
    skimc_p = PhotoUPSkimcoat.objects.all()
    return render(request, 'guesttemp/Skimcoat.html',{'skimc_p':skimc_p})

def sanitary_up(request):
    sanitary_up = PhotoUPSanitary.objects.all()
    return render(request, 'guesttemp/Sanitaryware.html',{'sanitary_up':sanitary_up})
   
""" def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('view_photos')
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'edit_photo  .html', {'form': form})

def delete_photo(request, pk):
    Photo.objects.get(pk=pk).delete()
    return redirect('view_photos') """