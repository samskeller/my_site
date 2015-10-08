from django.contrib import admin

from resume.models import Job
from resume.models import JobResponsibility
from resume.models import ResumeLink
from resume.models import School
from resume.models import SchoolDetail


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


admin.site.register(Job, JobAdmin)
admin.site.register(JobResponsibility, JobResponsibilityAdmin)
admin.site.register(ResumeLink, ResumeLinkAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(SchoolDetail, SchoolDetailAdmin)
