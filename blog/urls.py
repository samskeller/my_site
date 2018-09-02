from django.urls import include, path

from blog.views import BlogHome
from blog.views import BlogPost

app_name = 'blog'
urlpatterns = [
    path(r'', BlogHome.as_view(), name="blog_list"),
    path(r'posts/<slug:title>', BlogPost.as_view(), name='blog_post'),
]
