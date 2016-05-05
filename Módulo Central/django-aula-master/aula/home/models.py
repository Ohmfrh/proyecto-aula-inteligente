from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Pipeline(models.Model):
    pipe = models.CharField(max_length=5000)
