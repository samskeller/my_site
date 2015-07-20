from django.conf.urls import include, url

from blog.views import BlogHome

urlpatterns = [
    url(r'^$', BlogHome.as_view(), name="blog"),
]
