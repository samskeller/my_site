from django.shortcuts import render
from django.views.generic import View

from blog.models import Post

class BlogHome(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-date_created')[:20]
        return render(request, 'blog.html', {'posts': posts})
