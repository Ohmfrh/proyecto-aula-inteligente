from __future__ import unicode_literals

from django.db import models
from usuarios.models import Usersys
from multimedia.models import Server


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    server = models.ForeignKey(Server, blank=True, null=True)
    users = models.ManyToManyField(Usersys, through='UserImage', blank=True)

    def __str__(self):
        return self.name


class UserImage(models.Model):
    user = models.ForeignKey(Usersys)
    image = models.ForeignKey(Image)
