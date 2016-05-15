from django.db import models
from django.core.exceptions import ValidationError

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


class PostImage(BaseModel):
    '''
    A model for including images into blog Posts
    '''
    image = models.ImageField()
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='images')
    reference = models.CharField(max_length=100)

    def __str__(self):
        return '{} on Post {}'.format(self.reference, self.post.pk)

    def save(self, *args, **kwargs):
        conditions = models.Q(post=self.post, reference=self.reference)
        if self.pk:
            conditions &= ~models.Q(pk=self.pk)

        # Look to see if any PostImages with this reference already exist for
        # this post and if so raise a ValidationError
        if PostImage.objects.filter(conditions).exists():
            raise ValidationError("A PostImage with that reference already exists for this post")

        super(PostImage, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post Image'
        verbose_name_plural = 'Post Images'


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='comments')
    text = models.TextField()
    allowed = models.BooleanField(default=True)

    def __str__(self):
        return 'Comment {} on Post {}'.format(self.pk, self.post.pk)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
