from __future__ import unicode_literals

from django.db import models
from multimedia.models import Server
from usuarios.models import Usersys


# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    server = models.ForeignKey(Server, blank=True, null=True)
    users = models.ManyToManyField(Usersys, through='UserSong', blank=True)

    def __str__(self):
        return self.name


class UserSong(models.Model):
    user = models.ForeignKey(Usersys)
    song = models.ForeignKey(Song)

