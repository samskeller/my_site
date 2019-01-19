from django.shortcuts import render
from django.views.generic import View

from person_details.models import PersonDetail

class Home(View):
    def get(self, request, *args, **kwargs):
        my_description = PersonDetail.objects.filter(detail_type='description').first()
        return render(request, 'index.html', {'my_description': my_description})

