from django.db import models

from common.models import BaseModel


class Link(BaseModel):
    url = models.URLField()
    title = models.CharField(max_length=30)
    icon = models.ImageField(upload_to='link_icons/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Make sure the link starts with 'http://' so it's a valid external link
        try:
            if self.url.index('http://') != 0:
                self.url = 'http://' + self.url
        except ValueError:
            self.url = 'http://' + self.url

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
