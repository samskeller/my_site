from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.exceptions import MultipleObjectsReturned
from django.contrib.staticfiles.templatetags.staticfiles import static

from blog.models import Post
from blog.models import PostImage

import re

class BlogHome(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-date_created')[:20]
        return render(request, 'blog_list.html', {'posts': posts})

class BlogPost(View):
    def get(self, request, *args, **kwargs):
        slug = kwargs.pop('title', None)
        if not id:
            posts = Post.objects.all().order_by('-date_created')[:20]
            return render(request, 'blog_list.html', {'posts': posts})

        try:
            post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            posts = Post.objects.all().order_by('-date_created')[:20]
            return render(request, 'blog_list.html', {'posts': posts})

        if post.external_url:
            return redirect(post.external_url)

        post_text = post.text

        # Look for image tags in the post that need their "src" attributes to
        # be replaced. I put in the "reference" of the PostImage and so I'll
        # look for that inside a familiar Django "{% image <text> %} format
        matches = re.findall('{% image (.*) %}', post_text)
        for match in matches:
            try:
                post_image = post.images.get(reference=match)
            except (PostImage.DoesNotExist, MultipleObjectsReturned):
                continue

            # Get the static version of this URL
            static_image_url = static(post_image.image.url)

            post_text = post_text.replace('{{% image {} %}}'.format(match), static_image_url)

        return render(request, 'blog_post.html', {'post': post, 'post_text': post_text})
