from django.db import models

from common.models import BaseModel

from common.tools import clean_url


class Link(BaseModel):
    title = models.CharField(max_length=30)
    url = models.URLField()
    svg = models.TextField()

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
        return 'Click on {} Link'.format(self.link)

    class Meta:
        verbose_name = 'Link Click'
        verbose_name_plural = 'Link Clicks'

class PersonDetail(BaseModel):
    detail_type = models.CharField(max_length=40, unique=True)
    detail_value = models.TextField()

    def __str__(self):
        return '{} Person Detail'.format(self.detail_type)

    class Meta:
        verbose_name = 'Person Detail'
        verbose_name_plural = 'Person Details'
