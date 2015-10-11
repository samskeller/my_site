from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from my_site.views import Home
from person_details.views import AboutMe

admin.autodiscover()

urlpatterns = [
    url(r'^/$', Home.as_view(), name="home"),
    url(r'^$', Home.as_view(), name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', include('person_details.urls', namespace="person_details")),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^resume/', include('resume.urls', namespace="resume")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
