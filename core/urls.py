
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns= []

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
