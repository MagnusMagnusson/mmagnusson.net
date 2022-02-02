from email.policy import HTTP
from django.http import HttpResponse
from django.template import loader
import random
from contact.forms import ContactMeForm

def landing(request):
    temp = loader.get_template('ms_landing.html')
    return HttpResponse(temp.render({}, request))

def contact_me(request):
    if request.method =="GET":
        temp = loader.get_template('ms_contact.html')
        form = ContactMeForm()
        cont={
            "form":form
        }
        return HttpResponse(temp.render(cont, request))