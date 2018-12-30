from django.conf.urls import url

from . import views

urlpatterns = [
	#HTML REQUESTS
    url(r'um', views.about, name='um'),
    url(r'about$', views.about, name='about'),
    url(r'contact$', views.contact, name='samband'),
    url(r'samband', views.contact, name='samband'),
    url(r'^index$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^favicon.ico$', views.favico, name='favico'),
] 