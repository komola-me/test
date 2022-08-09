from django.contrib import admin
from event.models import Tag, Event

# Register your models here.
admin.site.register(Tag)
admin.site.register(Event)