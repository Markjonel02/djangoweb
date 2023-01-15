from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from mainweb import views as mainup
from mainweb.models import PhotoUP



# Create your views here.
def base(request):
    if request.method == 'GET':     
     posts = PhotoUP.objects.all()
    return render(request,'guesttemp/base.html',{'posts':posts})  

""" def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('view_photos')
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'edit_photo.html', {'form': form})

def delete_photo(request, pk):
    Photo.objects.get(pk=pk).delete()
    return redirect('view_photos') """