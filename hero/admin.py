from django.contrib import admin

from .models import Hero, HeroImages

class HeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_timestamp', 'is_active',)
    list_editable = ('is_active',)

admin.site.register(Hero, HeroAdmin)

admin.site.register(HeroImages)
