from django.urls import path
from .import views as admin_views
from django.conf.urls.static import static
from django.conf import settings
from CustomerProfile import urls 
from Usermanagement import urls
from ProductManagement import urls
from PointOfSale import urls
urlpatterns = [
        
        path('',admin_views.dashboard, name="dash"),
        
     
 ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT) 