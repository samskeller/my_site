from django.urls import include, path

from resume.views import ResumeView

app_name = 'resume'
urlpatterns = [
    path(r'', ResumeView.as_view(), name="resume"),
]
