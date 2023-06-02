from django.urls import path
from .import views
urlpatterns = [
    path('usermanagement/', views.usermanagement, name='userman'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('deactivate/<int:id>', views.deactivate_user, name='deactivate'),
    path('activate/<int:id>', views.activate_user, name='activate'),
    
]