from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError

from common.models import BaseModel

from common.tools import clean_url


class Job(BaseModel):
    '''
    Model for storing information on a position held at an organization.
    '''
    title = models.CharField(max_length=100)
    employer = models.CharField(max_length=100)
    employer_link = models.URLField(max_length=200)
    date_started = models.DateTimeField()
    date_ended = models.DateTimeField(null=True, blank=True)
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
    date_ended = models.DateTimeField(null=True, blank=True)

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


class SkillType(BaseModel):
    '''
    Model for defining the types of skills that the person has so those skills can be 
    grouped into sections
    '''
    name = models.CharField(max_length=64)
    order = models.IntegerField(default=0)

    def __str__(self, *args, **kwargs):
        return self.name

    def save(*args, **kwargs):
        if self.pk and SkillType.objects.filter(Q(order=self.order) & ~Q(pk=self.pk)).exists():
            raise ValidationError("Order {} already in use".format(self.order))
        return super(SkillType, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Skill Type'
        verbose_name_plural = 'Skill Types'


class Skill(BaseModel):
    '''
    Model for listing the skills that a person have, grouped by their types
    '''
    skill_type = models.ForeignKey(SkillType, on_delete=models.PROTECT, related_name='skills')
    key = models.CharField(max_length=64)
    value = models.TextField()

    def __str__(self, *args, **kwargs):
        return self.key

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

