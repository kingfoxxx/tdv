from django.contrib import admin

from .models import Contacts, ContactText

admin.site.register(Contacts)
admin.site.register(ContactText)
