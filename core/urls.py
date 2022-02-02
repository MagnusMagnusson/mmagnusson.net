from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path, include
from main_site import views as mainSite
from contact.urls import urlpatterns as contact_urls

urlpatterns= [
    re_path('admin/', admin.site.urls),   
    re_path('contact', mainSite.contact_me),   
    re_path('', mainSite.landing),   
]

