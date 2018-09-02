from django.urls import include, path

from .views import AboutMe
from .views import LinkList

app_name = 'person_deatils'
urlpatterns = [
    path(r'', AboutMe.as_view(), name="about"),
    path(r'links', LinkList.as_view(), name='link_list'),
]
