from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from main_site import views as mainSite
from cv import views as cvViews

urlpatterns= [
    path('admin/', admin.site.urls),     
    path('contact/', mainSite.contact_me),   
    path('about/cv.pdf', cvViews.cvPDF),     
    path('about/', mainSite.about),    
    path('portfolio/', mainSite.portfolio),   
    path('portfolio/<int:id>', mainSite.portfolio),   
    path('', mainSite.landing),   
]

