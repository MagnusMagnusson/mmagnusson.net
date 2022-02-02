from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from contact.views import contact_me

urlpatterns= [
    path('/', contact_me),
    path('', contact_me)
]

