from django.contrib import admin
from .models import Talks, Event, Shift, Location, Person

# Register your models here.


@admin.register(Talks)
class TalksAdmin(admin.ModelAdmin):
    list_display = ('date', 'start', 'name', 'speaker', 'talk_mod1', 'talk_mod2', 'youtube_link')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'start','name', 'event_mod1', 'event_mod2', 'host', 'link')
    list_filter = ('date',)
    ordering = ('date', 'start')


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('location', 'date', 'start', 'shift_worker', 'end', 'date')
    list_filter = ('location', 'date')
    ordering = ('date','start')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'discord', 'email', 'is_volunteer', 'is_staff', 'is_speaker')
    list_filter = ('is_volunteer', 'is_staff', 'is_speaker')