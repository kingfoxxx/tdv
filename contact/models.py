from django.db import models
from django.core.validators import FileExtensionValidator

from tinymce.models import HTMLField

class Contacts(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    icon = models.FileField(upload_to='contacts_icons', blank=True, null=True, validators=[FileExtensionValidator(['svg', 'png'])])
    active = models.BooleanField(default=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['-id']

    def __str__(self):
        return self.name

class ContactText(models.Model):
    image = models.ImageField(upload_to='contact_image', blank=True, validators=[FileExtensionValidator(['jpg'])])
    header = models.CharField(max_length=75, blank=True)
    body = HTMLField()

    class Meta:
        verbose_name = 'ContactText'
        verbose_name_plural = 'ContactText'
        ordering = ['-id']

    def __str__(self):
        return self.header
