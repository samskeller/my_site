from django.db import models

from common.models import BaseModel

from common.tools import clean_url


class Link(BaseModel):
    url = models.URLField()
    title = models.CharField(max_length=30)
    icon = models.ImageField(upload_to='link_icons/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.url = clean_url(self.url)
        return super(Link, self).save(*args, **kwargs)

    def __str__(self):
        return '{} Link'.format(self.title)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

class LinkClick(BaseModel):
    link = models.ForeignKey(Link, on_delete=models.PROTECT)

    def __str__(self):
        return 'Click on {} Link'.format(link)

    class Meta:
        verbose_name = 'Link Click'
        verbose_name_plural = 'Link Clicks'
