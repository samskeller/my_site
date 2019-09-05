from django.urls import include, path

from .views import AboutMe

app_name = 'person_details'
urlpatterns = [
    path(r'', AboutMe.as_view(), name="about"),
]
