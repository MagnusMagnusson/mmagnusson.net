from django.conf.urls import url

from . import views

urlpatterns = [
	#HTML REQUESTS
    url(r'', views.index, name='index'),
] 