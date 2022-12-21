from django.urls import path
from .import views as admin_views
 
urlpatterns = [
  
    path('',admin_views.dashboard, name="dashboard"),    
    path('index/',admin_views.index, name="index"),

 ]