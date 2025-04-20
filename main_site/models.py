from django.db import models
from django.utils.timezone import now
from django.db.models import Sum

class VisitorCount(models.Model):
    day = models.DateField(default = now)
    count = models.IntegerField(default = 0)

    def increment(request, response):
        cookie = request.COOKIES.get('visit', None)
        today = now().date()
        if cookie == None:
            c = VisitorCount.objects.filter(day = today).exists()
            if c:
                c = VisitorCount.objects.get(day = today)
                c.count = c.count + 1
                c.save()
            else:
                c = VisitorCount(count = 1, day = today)
                c.save()
            response.set_cookie('visit', c.count)
            return True
        return False

        
    def adjustedCount(request):
        cookie = request.COOKIES.get('visit', None)
        extra = 1 if cookie == None else 0
        sum_dict = VisitorCount.objects.aggregate(Sum('count'))
        sum = sum_dict['count__sum'] if sum_dict['count__sum'] else 0
        return sum + extra
