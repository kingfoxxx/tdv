from django.db import models
from django.core.validators import FileExtensionValidator

from tinymce.models import HTMLField

class Hero(models.Model):
    title = models.CharField(max_length=50, blank=True)
    subtitle = models.CharField(max_length=50, blank=True)
    description = HTMLField()
    logo = models.ImageField(upload_to='hero_logo', blank=True, validators=[FileExtensionValidator(['png'])])
    explore_button_text = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Hero'
        verbose_name_plural = 'Hero'
        db_table = 'Hero'
        ordering = ('created_timestamp',)

class HeroImages(models.Model):
    image = models.ImageField(upload_to='hero_images', validators=[FileExtensionValidator(['jpg'])])
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    uploaded_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'HeroImage'
        verbose_name_plural = 'HeroImages'
        db_table = 'HeroImage'
        ordering = ('created_timestamp',)

