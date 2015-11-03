from django.shortcuts import render
from django.views.generic import View

from .models import LinkType

class AboutMe(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')


class LinkList(View):
    def get(self, request, *args, **kwargs):
        link_types = LinkType.objects.all()
        return render(request, 'link_list.html', {'link_types': link_types})
