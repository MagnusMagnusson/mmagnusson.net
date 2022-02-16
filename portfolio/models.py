from django.db import models
from media_app.models import Image, Thumbnail
from cv.models import Skill

class WorkLink(models.Model):
    title = models.CharField(max_length=64)
    link = models.URLField()

class Group(models.Model):
    title = models.CharField(max_length = 64)
    description_en = models.TextField(max_length = 512)
    description_is = models.TextField(max_length = 512)

    def __str__(self):
        return self.title

class Work(models.Model):
    title = models.CharField(max_length=64)    
    subgroup = models.CharField(max_length=64, default="Misc")    
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    description_en = models.TextField(max_length = 512)
    description_is = models.TextField(max_length = 512)
    thumbnail = models.ForeignKey(Thumbnail, null=True, on_delete=models.SET_NULL)
    image = models.ManyToManyField(Image)
    links = models.ManyToManyField(WorkLink)
    skill = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title

