from django.conf.urls import include, url
from django.contrib import admin

from my_site.views import Home
from person_details.views import AboutMe

import blog.urls

admin.autodiscover()

urlpatterns = [
    url(r'^/$', Home.as_view(), name="home"),
    url(r'^$', Home.as_view(), name="home"),
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^about/$', AboutMe.as_view(), name="about"),
    url(r'^blog/', include(blog.urls, namespace="blog")),
]
