from django.shortcuts import render
from django.views.generic import View

from resume.models import Job
from resume.models import JobResponsibility
from resume.models import ResumeLink
from resume.models import School
from resume.models import SchoolDetail


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        jobs = Job.objects.all().order_by('-date_started')
        resume_links = ResumeLink.objects.all()
        schools = School.objects.all().order_by('-date_started')

        return render(request, 'resume.html', {'jobs': jobs, 'resume_links': resume_links, 'schools': schools})
