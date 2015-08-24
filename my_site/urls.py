from django.conf.urls import include, url
from django.contrib import admin

from my_site.views import Home
from person_details.views import AboutMe

admin.autodiscover()

urlpatterns = [
    url(r'^/$', Home.as_view(), name="home"),
    url(r'^$', Home.as_view(), name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', include('person_details.urls', namespace="person_details")),
    url(r'^blog/', include('blog.urls', namespace="blog")),
]
