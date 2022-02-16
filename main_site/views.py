from email.policy import HTTP
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
import random
from contact.forms import ContactMeForm
from contact.models import ContactResponse
from cv.models import Skill
from portfolio.models import Work, Group


def about(request):
    temp = loader.get_template('ms_about.template')
    skillDict = Skill.skillDict()
    return HttpResponse(temp.render({"skills":skillDict}, request))
    
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
            temp = loader.get_template('ms_contact_thanks.template')
            return HttpResponse(temp.render({}, request))
        else:
            return render_contact(request, True)

def landing(request):
    temp = loader.get_template('ms_landing.template')
    return HttpResponse(temp.render({}, request))

def portfolio(request, id = None):
    if id == None:
        temp = loader.get_template('ms_portfolio.template')
        groups = Group.objects.all()
        work = Work.objects.all().order_by("subgroup")
    
        group_list = [{
            "group" : g,
            "jobs": [x for x in work if x.group == g]
        } for g in groups if g.work_set.count() > 0]

        return HttpResponse(temp.render({
            "group_list":group_list
        }, request))
    else:
        work = get_object_or_404(Work,id=id)
        temp = loader.get_template('ms_work.template')
        return HttpResponse(temp.render({
            "work":work
        }, request))

def render_contact(request, is_failed = False):
    temp = loader.get_template('ms_contact.template')
    form = ContactMeForm()
    cont={
        "form":form,
        "failed_captcha" : is_failed
    }
    return HttpResponse(temp.render(cont, request))
