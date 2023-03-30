from django.db import models
from django.core.validators import FileExtensionValidator

from tinymce.models import HTMLField

class Genre(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Genre'
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ('-created_timestamp',)

    def __str__(self):
        return self.name

class Track(models.Model):
    title = models.CharField(max_length=200)
    track = models.FileField(upload_to='tracks', blank=True, validators=[FileExtensionValidator(['wav', 'mp3'])])
    description = HTMLField()
    image = models.ImageField(upload_to='track_arts', blank=True, validators=[FileExtensionValidator(['png','jpg'])])
    is_active = models.BooleanField(default=True)
    genre = models.ManyToManyField(Genre, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Tracks'
        verbose_name = 'Track'
        verbose_name_plural = 'Tracks'
        ordering = ('-created_timestamp',)

    def __str__(self):
        return self.title
