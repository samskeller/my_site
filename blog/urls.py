from django.conf.urls import include, url

from blog.views import BlogHome
from blog.views import BlogPost

urlpatterns = [
    url(r'^$', BlogHome.as_view(), name="blog_list"),
    url(r'posts/(?P<slug>[\w-]+)/$', BlogPost.as_view(), name='blog_post'),
]
