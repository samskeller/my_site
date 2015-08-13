from django.shortcuts import render
from django.views.generic import View

from blog.models import Post

class BlogHome(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-date_created')[:20]
        return render(request, 'blog_list.html', {'posts': posts})

class BlogPost(View):
    def get(self, request, *args, **kwargs):
        slug = kwargs.pop('slug', None)
        if not id:
            posts = Post.objects.all().order_by('-date_created')[:20]
            return render(request, 'blog_list.html', {'posts': posts})

        try:
            post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            posts = Post.objects.all().order_by('-date_created')[:20]
            return render(request, 'blog_list.html', {'posts': posts})
            
        return render(request, 'blog_post.html', {'post': post})
