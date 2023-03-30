from django.db import models
from django.core.validators import FileExtensionValidator

from tinymce.models import HTMLField

class About(models.Model):
    image = models.ImageField(upload_to='about_images',  blank=True, validators=[FileExtensionValidator(['jpg'])])
    header = models.CharField(max_length=75)
    body = HTMLField()

    class Meta:
        verbose_name = 'About Me'
        verbose_name_plural = 'About Me'
        ordering = ['-id']

    def __str__(self):
        return self.header
