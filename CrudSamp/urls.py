from django.urls import path
from  .import views as crud_views

urlpatterns = [
   path('',crud_views.listcustomer,name="customers_list"),
   path('create/',crud_views.createcustomer,name='customers_create'),
   path('delete/<int:pk>/',crud_views.deletecustomer,name="customers_delete"),
   path('update/<int:pk>/',crud_views.update,name="customers_update"),
]