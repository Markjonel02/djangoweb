from django.urls import path
from .import views as guest_views
from mainweb import views as gallery #import the views of mainweb into the  guestpageviews
""" from django.conf.urls.static import static
from django.conf import settings
#create urls here """
urlpatterns = [
      path('',guest_views.base, name='base'),
      
      #path('register',guest_views.register, name='register'),
]
""" if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT) """