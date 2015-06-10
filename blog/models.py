from django.db import models

from common.models import BaseModel

class Post(BaseModel):
    title = models.CharField(max_length=100)
    text = models.TextField()
    slug = models.SlugField(max_length=60)
    
    def __str__(self):
        return 'Post {}: {}'.format(self.pk, self.title)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='comments')
    text = models.TextField()
    allowed = models.BooleanField(default=True)

    def __str__(self):
        return 'Comment {} on Post {}'.format(self.pk, self.post.pk)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
