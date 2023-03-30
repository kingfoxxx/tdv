from django.contrib import admin

from .models import Genre, Track

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'id')
    list_editable = ('is_active',)
    search_fields = ('name',)
    ordering = ('created_timestamp',)

admin.site.register(Genre, GenreAdmin)

class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'id')
    list_editable = ('is_active',)
    search_fields = ('title',)
    ordering = ('created_timestamp', 'updated_timestamp')

admin.site.register(Track, TrackAdmin)
