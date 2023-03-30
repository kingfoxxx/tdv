from django.db import models
from django.core.validators import FileExtensionValidator

from tinymce.models import HTMLField

class Support(models.Model):
    image = models.ImageField(upload_to="support_images", blank=True, validators=[FileExtensionValidator(['jpg'])])
    header = models.CharField(blank=True, max_length=75)
    body = HTMLField()

    class Meta:
        verbose_name = 'Support Me'
        verbose_name_plural = 'Support Me'
        ordering = ['-id']

    def __str__(self):
        return self.header


class Donation(models.Model):
    amount = models.PositiveIntegerField()
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    reference = models.CharField(max_length=200)
    transanction_id = models.CharField(max_length=55)
    transanction_message = models.CharField(max_length=255)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Donation'
        verbose_name_plural = 'Donations'
        ordering = ['-created_timestamp']

    def __str__(self):
        return self.reference
