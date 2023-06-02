from django.shortcuts import render,redirect,HttpResponseRedirect, reverse,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib import messages

# Create your views here.

 # --- Start usermanagement ---
@login_required()
def usermanagement(request):
    custom_ucf = CustomUserCreationForm()
    
    if request.method == "POST":
        custom_ucf = CustomUserCreationForm(request.POST)
        if custom_ucf.is_valid():
            custom_ucf.save()
            messages.success(request,'New user has been added!')
            print("save")
            custom_ucf = CustomUserCreationForm()
            return HttpResponseRedirect(reverse('usermanagement'))
    
    return render(request,'Usermanagement/usermanagement.html',{'custom_ucf':custom_ucf, 'users':CustomUser.objects.all()})
 
 
@login_required()
def edit(request,id): 
    c = get_object_or_404(CustomUser,id=id)
    custom_uchf = CustomUserChangeForm(instance=c)
    custom_uchf.fields['username'].widget.attrs.update({'readonly':True}) #setting the username as readonly 
    if request.method == 'POST':
        custom_uchf = CustomUserChangeForm(request.POST, instance=c)
        if custom_uchf.is_valid():
            custom_uchf.save()
            messages.success(request,'User :'+' '+ c.username + ' is successfully updated')
            return redirect('userman')
        
    context = {
        'custom_uchf':custom_uchf,
        'c':c
    }    
    return render(request, 'Usermanagement/edit.html',context)

@login_required
def deactivate_user(request, id):
    users = CustomUser.objects.get(id=id)
    users.is_active = False
    users.save()
    messages.info(request,'User: ' + ' ' + users.username + " is now deactivated"  )
    return  redirect('userman')



@login_required
def activate_user(request, id):
    users = CustomUser.objects.get(id=id)
    users.is_active = True
    users.save()
    messages.success(request,'User: '+ '' + users.username + " is now activated")
    return redirect('userman')
# --- End usermanagement ---           