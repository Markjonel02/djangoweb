from django.urls import path
from .import views as Userpage_views
#from mainweb import views as Mainweb_views


urlpatterns = [
    path('',Userpage_views.login_request,name='login'),
#    path('register/',Userpage_views.register_request ,name='register'),
    path('logout/',Userpage_views.logout_request, name="logout"),
   
    
]