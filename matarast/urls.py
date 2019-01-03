from django.conf.urls import url

from . import views

urlpatterns = [
	#HTML REQUESTS 
    url(r'^innskra$', views.login, name='login'),
    url(r'^eg$', views.profile, name='profile'),
	
    url(r'^api/innskra$', views.api_log_in, name='api_login'),

    url(r'^$', views.index, name='index'),

] 