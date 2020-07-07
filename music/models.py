from django.db import models
from django.urls import reverse
import os


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=250)
    album_logo = models.FileField(upload_to='images')

    def get_absolute_url(self):
        return reverse('music:index')

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    song_title = models.CharField(max_length=250)
    song_file = models.FileField(upload_to='songs')

    def extension(self):
        name, extension = os.path.splitext(self.song_file.name)
        return extension[1:]

    def __str__(self):
        return self.song_title + ' - ' + self.artist
