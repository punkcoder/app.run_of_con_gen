from django.contrib import admin
from .models import Talks, Event, Shift

# Register your models here.
@admin.register(Talks)
class TalksAdmin(admin.ModelAdmin):
    list_display = ('start', 'name', 'speaker', 'mod1_discord', 'mod2_discord', 'youtube_link')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('start','name', 'mod1_discord','host', 'link')

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('location', 'start', 'end', 'discord_username', 'date')
    list_filter = ('location', 'date')