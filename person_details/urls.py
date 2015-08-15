from django.conf.urls import include, url

from .views import AboutMe
from .views import LinkList

urlpatterns = [
    url(r'^$', AboutMe.as_view(), name="blog_list"),
    url(r'^links$', LinkList.as_view(), name='link_list'),
]
