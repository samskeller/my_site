from django.db import models

# Create your models here.

class BaseModel(models.Model):
    date_last_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
