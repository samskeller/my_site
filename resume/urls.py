from django.conf.urls import include, url

from resume.views import ResumeView

urlpatterns = [
    url(r'^$', ResumeView.as_view(), name="resume"),
]
