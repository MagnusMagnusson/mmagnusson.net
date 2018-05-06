from django.conf.urls import url

from . import views

urlpatterns = [
	#HTML REQUESTS
    url(r'^(index)?$', views.index, name='index'),
] 