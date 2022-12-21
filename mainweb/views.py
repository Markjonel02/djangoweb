from django.shortcuts import render, redirect, get_object_or_404 
#from .models import Entry, Profile
""" from .forms import  NewUserForm 
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse """
""" 
from django.contrib.auth.models import User
# Create your views here.
def index(request):
   form = AddEntry(request.POST or None)
   context = {'entries':Entry.objects.all(), 'form':form } 
   
   if request.method == 'POST':
       if form.is_valid():
           entry = form.save(commit=False)
           entry.author = request.user
           entry.save()
           return redirect('index')
       
   return render(request, 'index.html', context )

    
   
def add(request):
    
    return render(request, 'add.html')
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Entry, id = id)
 
 
    if request.method =='POST':
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return redirect('index')
 
    return render(request, 'delete.html', context)
 """""" 
    # update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Entry, id = id)
 
    # pass the object as instance in form
    form = AddEntry(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('index')
 
    # add form dictionary to context
    context['form'] = form
 
    return render(request, 'update.html', context)

 """


def dashboard(request):
    return render(request, 'Dashboard.html')


def index(request):
    return render(request, 'index.html')
""" 
#Register
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('dashboard')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name='users/register.html', context={'form':form})

    #login Form

def login_request(request):

	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('dashboard')    
			else:
				messages.error(request,'Invalid username or password.')
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name='users/login.html', context={'form':form})




def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('login')  """
""" 
@login_required
def profile(request):

  context = {
    'profiles': Profile.objects.all(),
    'entries': Entry.objects.all(),
  }
  return render(request, 'profile.html', context)""" 
 
 
""" def EditProfile(request):
     profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
     if request.method == 'POST':
      if profile_form.is_valid():
       profile_form.save()
       messages.success(request, 'Your profile is updated successfully')
       return redirect(to='profile')
     else:
      profile_form = ProfileForm(instance=request.user.profile)
     return render(request, 'edit.html', { 'form' : profile_form}) """ 