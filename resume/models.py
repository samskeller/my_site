from django.db import models

from common.models import BaseModel

class Job(BaseModel):
    '''
    Model for storing information on a position held at an organization.
    '''
    title = models.CharField(max_length=100)
    employer = models.CharField(max_length=100)
    employer_link = models.URLField(max_length=200)
    date_started = models.DateTimeField()
    date_ended = models.DateTimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return '{} at {}'.format(self.title, self.employer)

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'


class JobResponsibility(BaseModel):
    '''
    Model for the individual responsibilities held at a particular job
    '''
    job = models.ForeignKey(Job, on_delete=models.PROTECT, related_name='responsibilities')
    text = models.TextField()

    def __str__(self):
        return 'Responsibility {} at Job {}'.format(self.pk, self.job.pk)

    class Meta:
        verbose_name = 'Job Responsibility'
        verbose_name_plural = 'Job Responsibilities'


class ResumeLink(BaseModel):
    '''
    Model for the various links needed for a resume (LinkedIn, GitHub, etc)
    '''
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.url = clean_url(self.url)
        return super(ResumeLink, self).save(*args, **kwargs)

    def __str__(self):
        return '{} Resume Link'.format(self.title)

    class Meta:
        verbose_name = 'Resume Link'
        verbose_name_plural = 'Resume Links'


class School(BaseModel):
    '''
    Model for the schools attended and the degrees earned at those schools
    '''
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    degree = models.CharField(max_length=200)
    date_started = models.DateTimeField()
    date_ended = models.DateTimeField()

    def __str__(self, *args, **kwargs):
        return 'School: {}'.format(self.name)

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'


class SchoolDetail(BaseModel):
    '''
    Model for specific details on a School attended -- coursework, honors, theses, etc
    '''
    school = models.ForeignKey(School, on_delete=models.PROTECT, related_name='details')
    key = models.CharField(max_length=30)
    value = models.TextField()

    def __str__(self, *args, **kwargs):
        return '{} for {}'.format(self.key, self.school.name)

    class Meta:
        verbose_name = 'School Detail'
        verbose_name_plural = 'School Details'

