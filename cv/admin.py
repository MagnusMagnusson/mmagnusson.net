from django.contrib import admin
from cv.models import Section, BaseInfo, BigSectionEntry, Skill

class SectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Section, SectionAdmin)


class BigSectionEntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(BigSectionEntry, BigSectionEntryAdmin)


class BaseInfoAdmin(admin.ModelAdmin):
    pass
admin.site.register(BaseInfo, BaseInfoAdmin)


class SkillAdmin(admin.ModelAdmin):
    pass
admin.site.register(Skill, SkillAdmin)