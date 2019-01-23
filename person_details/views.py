from django.shortcuts import render
from django.views.generic import View

from .models import PersonDetail

class AboutMe(View):
    def get(self, request, *args, **kwargs):
        my_description = PersonDetail.objects.filter(detail_type='description').first()

        return render(request, 'about.html', {'my_description': my_description})
