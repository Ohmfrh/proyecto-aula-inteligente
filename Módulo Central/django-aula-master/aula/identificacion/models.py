from __future__ import unicode_literals

import sys    # sys.setdefaultencoding is cancelled by site.py
reload(sys)    # to re-enable sys.setdefaultencoding()
sys.setdefaultencoding('utf-8')

from django.db import models
from usuarios.models import Usersys


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Identify(models.Model):
    string = models.CharField(max_length=255)
    usersys = models.ForeignKey(Usersys, on_delete=models.CASCADE, default=None, null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.string