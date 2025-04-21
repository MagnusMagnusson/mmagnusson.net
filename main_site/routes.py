from main_site import views as mainSite
from django.urls import path, include

urlpatterns = [
    path('', mainSite.landing),   
]