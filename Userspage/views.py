from django.shortcuts import render,redirect
#from .forms import  NewUserForm 
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Usermanagement import views
#from mainweb import views as Mainweb_views
# Create your views here.


    #login Form
login_required()
def login_request(request):
  
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('dash')
			else:
				messages.error(request,'Invalid username or password.')
		else:
     
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name='usertemp/login.html', context={'Login':form})
    


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('login') 
