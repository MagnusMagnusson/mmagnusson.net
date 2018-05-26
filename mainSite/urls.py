from django.conf.urls import url

from . import views

urlpatterns = [
	#HTML REQUESTS
    url(r'um$', views.about, name='um'),
    url(r'about$', views.about, name='about'),
    url(r'^(index)?$', views.index, name='index'),
] 