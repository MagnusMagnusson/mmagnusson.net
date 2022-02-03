from email.policy import HTTP
from django.http import HttpResponse
from django.template import loader
import random
from contact.forms import ContactMeForm
from contact.models import ContactResponse
from cv.models import Skill


def landing(request):
    temp = loader.get_template('ms_landing.html')
    return HttpResponse(temp.render({}, request))

def render_contact(request, is_failed = False):
    temp = loader.get_template('ms_contact.html')
    form = ContactMeForm()
    cont={
        "form":form,
        "failed_captcha" : is_failed
    }
    return HttpResponse(temp.render(cont, request))
def contact_me(request):
    if request.method == "GET":
        return render_contact(request)
    elif request.method == "POST":
        p = request.POST
        name = p["your_name"]
        email = p["your_email"]
        header = p["message_title"]
        body = p["your_message"]
        captcha = p["my_name"]
        success = ContactResponse.process(name, email, header, body, captcha)
        if success:
            temp = loader.get_template('ms_contact_thanks.html')
            return HttpResponse(temp.render({}, request))
        else:
            return render_contact(request, True)

def about(request):
    temp = loader.get_template('ms_about.html')
    skills = Skill.objects.all().order_by('-category','-value')
    skillDict = {}
    for s in skills:
        c = s.category
        print(s)
        if not c in skillDict:
            skillDict[c] = []
        skillDict[c].append([s.skill, s.value])
    return HttpResponse(temp.render({"skills":skillDict}, request))