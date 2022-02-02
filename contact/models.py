from django.db import models
from django.core.mail import send_mail
from django.conf import settings
import os
import re

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
        
        mess = ContactResponse(
            name = name,
            email = email,
            header = header,
            content = content
        )
        mess.save()
        if not settings.DEBUG: #Only send mail when we're allowed to send mail. 
            send_mail(
                'CONTACT FORM - ' + mess.header,
                "A new message was recieved via mmagnusson.net from "+mess.name+" => "+mess.email+" \n\n "+mess.content,
                settings.ADMIN_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=True,
            )
        return True
    
    def __str__(self):
        d = "[DONE]" if self.dealt_with else ""
        return d + self.name + " - " + self.header + "  ("+ str(self.date)+")"