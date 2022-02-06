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
    icon = models.CharField(max_length = 64, blank=True, default="")
    public = models.BooleanField(default = False)

    def __str__(self):
        return self.label + "("+(self.section.name if self.section else "")+")"

class References(models.Model):
    name = models.CharField(max_length = 64)
    job = models.CharField(max_length = 128)
    relation = models.CharField(max_length = 128)
    email = models.EmailField(max_length = 128, blank=True)
    phone = models.CharField(max_length = 128, blank=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length = 128, default="/")
    school = models.CharField(max_length = 128, default="/")
    start = models.CharField(max_length = 128, default="/")
    end = models.CharField(max_length = 128, default="/")

    def __str__(self):
        return self.degree + " @ " + self.school

class Experience(models.Model):
    workplace = models.CharField(max_length = 128, default="Company")
    position = models.CharField(max_length = 128, default="Position")
    description = models.TextField(max_length = 1024, default="description here. Lorem Ipsum sig dol loriet")
    start = models.CharField(max_length = 128, default="1995")
    end = models.CharField(max_length = 128, default="2100")

    def __str__(self):
        return self.position + " @ " + self.workplace

class Skill(models.Model):
    skill = models.CharField(max_length=28)
    category = models.CharField(max_length=28)
    value = models.IntegerField()

    def __str__(self):
        return self.skill + "-" + str(self.value) +"  ["+self.category+"]"

    @staticmethod
    def skillDict():
        skills = Skill.objects.all().order_by('-category','-value')
        skillDict = {}
        for s in skills:
            c = s.category
            if not c in skillDict:
                skillDict[c] = []
            skillDict[c].append([s.skill, s.value])
        return skillDict

class Description(models.Model):
    description = models.TextField(max_length = 512)

class Interest(models.Model):
    interest = models.CharField(max_length=16)

    def __str__(self):
        return self.interest