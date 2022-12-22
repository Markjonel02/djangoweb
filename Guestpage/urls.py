from django.urls import path
from .import views as guest_views

#create urls here
urlpatterns = [
      path('',guest_views.base, name='base'),
      #path('register',guest_views.register, name='register'),
]