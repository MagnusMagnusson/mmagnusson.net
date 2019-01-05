from django.conf.urls import url

from . import views

urlpatterns = [
	#HTML REQUESTS 
    url(r'^innskra$', views.login, name='login'),
    url(r'^eg$', views.profile, name='profile'),
    url(r'^hraefni/nytt$', views.ingredient_new, name='ingredient_new'),
	
    url(r'^api/innskra$', views.api_log_in, name='api_login'),
    url(r'^api/hraefni/nytt', views.api_ingredient_new, name='api_new_ingredient'),
	
    url(r'^$', views.index, name='index'),

] 