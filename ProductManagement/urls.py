from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
     # product management urls      
        path('Search/',views.Search,name='search'),
        path('products/',views.products,name='product_list'),
        path('add product/<int:id>/',views.add_stock,name='add_stock'),
        path('prod_edit/<int:id>/',views.product_edit,name='product_edit'),
        path('delete/<int:id>/',views.product_del,name='product_del'),
        path('archive/',views.archive,name='prod_arch'),
      
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)