from django.db import models
from django.forms import CharField

class Section(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    label = models.CharField(max_length=64, blank=False, null=False)
    ordering = models.IntegerField(default = 0)

    def __str__(self):
        return self.name + "("+str(self.ordering)+")"

class BaseInfo(models.Model):
    label = models.CharField(max_length=64, default="N/A")
    text = models.CharField(max_length = 128, default ="N/A", null = False, blank = False)
    section = models.ForeignKey(to=Section, on_delete=models.CASCADE)
    icon = models.URLField(blank=True, default="")
    public = models.BooleanField(default = False)

    def __str__(self):
        return self.label + "("+(self.section.name if self.section else "")+")"

class BigSectionEntry(models.Model):
    label = models.CharField(max_length=64, default="N/A")
    header = models.CharField(max_length=128)
    subheader = models.CharField(max_length=128)
    text = models.TextField(max_length=1000)
    section = models.ForeignKey(to=Section, on_delete=models.CASCADE)    

    def __str__(self):
        return self.label + "("+(self.section.name if self.section else "")+")"

class Skill(models.Model):
    skill = models.CharField(max_length=28)
    category = models.CharField(max_length=28)
    value = models.IntegerField()

    def __str__(self):
        return self.skill + "-" + str(self.value) +"  ["+self.category+"]"