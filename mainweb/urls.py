from django.urls import path
from .import views as admin_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
         # customers profile urls 
        path('',admin_views.dashboard, name="dash"),
        # CRUD 
        path('customers/',admin_views.custom_list, name="customer_list"),
        path('edit/<int:pk>/',admin_views.edit_customers,name="customer_edit"),
        path('del/<int:pk>/',admin_views.del_customers,name='customer_del'),
        
        #search (links)
        #path('search/',admin_views.search,name='search'),
              
        # product management urls 
        path('prod/',admin_views.product_list,name='product_list'),
        path('prod_edit/<int:pk>/',admin_views.product_edit,name='product_edit'),
        path('delete/<int:pk>/',admin_views.product_del,name='product_del'),
        path('archive/',admin_views.archive,name='prod_arch'),

        # user management urls 
        path('usermanagement/',admin_views.usermanagement,name='userman'),
        
       
       # Uploading imaage on Guestpage 
       path('uploadimg/',admin_views.adupload_image,name="upload")
 ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)