from email.policy import HTTP
from django.http import HttpResponse
from django.template import loader
from main_site.models import VisitorCount
from django.utils.timezone import now


def landing(request):
    temp = loader.get_template('ms_landing.html')
    count = VisitorCount.adjustedCount(request)
    order = request.COOKIES.get('visit', count)
    response = HttpResponse(temp.render({'count':count, 'order':order}, request))
    return response