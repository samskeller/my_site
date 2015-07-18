from django.shortcuts import render
from django.views.generic import View

class AboutMe(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')
