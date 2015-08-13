from django.shortcuts import render
from django.views.generic import View

from blog.models import Post

class Home(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-date_created')[:5]
        return render(request, 'index.html', {'posts': posts})

