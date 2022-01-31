from django.http import HttpResponse
from django.template import loader

def landing(request):
    temp = loader.get_template('ms_landing.html')
    return HttpResponse(temp.render({}, request))
