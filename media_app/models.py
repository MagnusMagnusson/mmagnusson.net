from pydoc import classname
from sre_constants import MAX_UNTIL
from django.db import models
import datetime
from django.conf import settings

def get_def_name(instance, filename):
    today = datetime.datetime.now()
    return type(instance).__name__+"/"+str(today.year)+"/"+str(today.month)+"/"+str(today.day)+"/"+filename

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to = get_def_name)
    def __str__(self):
        return self.title
        
    @property 
    def url(self):
        return settings.STATIC_URL[:-1] + self.image.url

class Thumbnail(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to = get_def_name)
    def __str__(self):
        return self.title
        
    @property 
    def url(self):
        return settings.STATIC_URL[:-1] + self.image.url