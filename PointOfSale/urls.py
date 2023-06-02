from django.urls import path
from .import views
urlpatterns = [
    path('pos/',views.pos,name='pos'),
    path('porcelain/',views.porcelain_up,name='por')

]