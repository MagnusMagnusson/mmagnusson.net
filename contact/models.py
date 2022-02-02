from django.db import models
import re

from contact.forms import ContactMeForm

class ContactResponse(models.Model):
    name = models.CharField(max_length=100, default="Null Person")
    email = models.EmailField(default="null@null.null")
    header = models.CharField(max_length=100, default="Null Header")
    content = models.TextField(max_length=1024, default="Null Content")
    date = models.DateTimeField(auto_now=True)
    dealt_with = models.BooleanField(default=False)

    @staticmethod
    def process(name, email, header, content, captcha):
        captcha = captcha.lower()
        if re.search('magnús',captcha) == None and re.search('magnus',captcha) == None:
            return False
        
        mess = ContactMeForm({
            "name": name,
            "email":email,
            "header":header,
            "content":content
        }).save()
        return True