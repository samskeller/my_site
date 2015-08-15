from django.shortcuts import render
from django.views.generic import View

from .models import Link

class AboutMe(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')


class LinkList(View):
    def get(self, request, *args, **kwargs):
        links = Link.objects.all()
        return render(request, 'link_list.html', {'links': links})
