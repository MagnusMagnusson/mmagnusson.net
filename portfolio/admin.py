from django.contrib import admin
from portfolio.models import Group, Work, WorkLink


class GroupAdmin(admin.ModelAdmin):
    pass
admin.site.register(Group, GroupAdmin)

class WorkAdmin(admin.ModelAdmin):
    pass
admin.site.register(Work, WorkAdmin)

class WorkLinkAdmin(admin.ModelAdmin):
    pass
admin.site.register(WorkLink, WorkLinkAdmin)