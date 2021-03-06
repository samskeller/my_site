from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from my_site.views import Home
from person_details.views import AboutMe, HireMe

admin.autodiscover()

urlpatterns = [
    path(r'', Home.as_view(), name="home"),
    path(r'admin/', admin.site.urls),
    path(r'about/', include('person_details.urls', namespace="person_details")),
    path(r'hire-me/', HireMe.as_view(), name="hire-me"),
    path(r'blog/', include('blog.urls', namespace="blog")),
    path(r'resume/', include('resume.urls', namespace="resume")),
    path(r'books/', include('highlights.urls', namespace="highlights")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
