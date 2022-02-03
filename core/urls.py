from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from main_site import views as mainSite

urlpatterns= [
    path('admin/', admin.site.urls),   
    path('contact/', mainSite.contact_me),   
    path('about/', mainSite.about),   
    path('', mainSite.landing),   
]

