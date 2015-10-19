from django.contrib import admin

from resume.models import Job
from resume.models import JobResponsibility
from resume.models import ResumeLink
from resume.models import School
from resume.models import SchoolDetail
from resume.models import SkillType
from resume.models import Skill


class JobAdmin(admin.ModelAdmin):
    #title = models.CharField(max_length=100)
    #employer = models.CharField(max_length=100)
    #employer_link = models.URLField(max_length=200)
    #date_started = models.DateTimeField()
    #date_ended = models.DateTimeField()
    #location = models.CharField(max_length=100)
    list_display = ('id', 'title', 'employer', 'date_started', 'date_created',)
    list_selected_display = list_display
    readonly_fields = ('date_created', 'date_last_modified',)


class JobResponsibilityAdmin(admin.ModelAdmin):
    #job = models.ForeignKey(Job, on_delete=models.PROTECT, related_name='responsibilities')
    #text = models.TextField()
    list_display = ('id', 'job', 'date_created',)
    list_select_display = list_display
    readonly_fields = ('date_created', 'date_last_modified',)


class ResumeLinkAdmin(admin.ModelAdmin):
    #url = models.URLField(max_length=200)
    #title = models.CharField(max_length=50)
    list_display = ('id', 'title', 'date_created',)
    list_selected_display = list_display
    readonly_fields = ('date_created', 'date_last_modified',)

class SchoolAdmin(admin.ModelAdmin):
    #name = models.CharField(max_length=100)
    #location = models.CharField(max_length=100)
    #degree = models.CharField(max_length=200)
    #date_started = models.DateTimeField()
    #date_ended = models.DateTimeField()
    list_display = ('id', 'name', 'date_started', 'date_ended', 'date_created',)
    list_selected_display = list_display
    readonly_fields = ('date_created', 'date_last_modified',)


class SchoolDetailAdmin(admin.ModelAdmin):
    #school = models.ForeignKey(School, on_delete=models.PROTECT, related_name='details')
    #key = models.CharField(max_length=30)
    #value = models.TextField()
    list_display = ('id', 'school', 'key', 'value', 'date_created',)
    list_selected_display = list_display
    readonly_fields = ('date_created', 'date_last_modified',)


class SkillInline(admin.StackedInline):
    model = Skill 

    def get_formset(self, request, obj=None, **kwargs):
        if obj:  # obj is not None, so this is a change page
            kwargs['extra'] = 0
        else:  # obj is None, so this is an add page
            kwargs['extra'] = 1
        return super(SkillInline, self).get_formset(request, obj, **kwargs)


class SkillTypeAdmin(admin.ModelAdmin):
    #name = models.CharField(max_length=64)
    list_display = ('id', 'name', 'date_created',)
    list_selected_display = list_display
    readonly_fields = ('date_created', 'date_last_modified',)
    inlines = [SkillInline,]


class SkillAdmin(admin.ModelAdmin):
    #skill_type = models.ForeignKey(SkillType, on_delete=models.PROTECT, related_name='skills')
    #key = models.CharField(max_length=64)
    #value = models.TextField()
    list_display = ('id', 'skill_type', 'key', 'date_created',)
    list_selected_display = list_display
    readonly_fields = ('date_created', 'date_last_modified',)


admin.site.register(Job, JobAdmin)
admin.site.register(JobResponsibility, JobResponsibilityAdmin)
admin.site.register(ResumeLink, ResumeLinkAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(SchoolDetail, SchoolDetailAdmin)
admin.site.register(SkillType, SkillTypeAdmin)
admin.site.register(Skill, SkillAdmin)
