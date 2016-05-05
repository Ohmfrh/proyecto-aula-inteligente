from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


LOGGED = (
    ('0', 'No'),
    ('1', 'Yes')
)


# Create your models here.
class Usersys(models.Model):
    name = models.CharField(max_length=50)
    last_names = models.CharField(max_length=100)
    date_added = models.DateField('Fecha de alta', auto_now=True)
    email = models.CharField(max_length=100)
    logged = models.CharField(max_length=1, choices=LOGGED, default=0)

    def __str__(self):
        return self.name + ' ' + self.last_names

