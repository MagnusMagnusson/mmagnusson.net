from django.contrib import admin
from contact.models import ContactResponse

class ContactResponseAdmin(admin.ModelAdmin):
    pass
admin.site.register(ContactResponse, ContactResponseAdmin)
