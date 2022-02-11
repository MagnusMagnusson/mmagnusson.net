from django.contrib import admin
from cv.models import Section, BaseInfo, Education, Skill, References, Experience, Description, Interest

class SectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Section, SectionAdmin)


class EducationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Education, EducationAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Experience, ExperienceAdmin)

class DescriptionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Description, DescriptionAdmin)

class BaseInfoAdmin(admin.ModelAdmin):
    pass
admin.site.register(BaseInfo, BaseInfoAdmin)

class ReferenceAdmin(admin.ModelAdmin):
    pass
admin.site.register(References, ReferenceAdmin)

class SkillAdmin(admin.ModelAdmin):
    pass
admin.site.register(Skill, SkillAdmin)


class InterestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Interest, InterestAdmin)