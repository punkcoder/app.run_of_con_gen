from django.db import models

# Create your models here.


class Talks(models.Model):
    name = models.CharField(max_length=500,blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    start = models.TimeField(blank=False, null=False)
    end = models.TimeField(blank=False, null=False)
    mod1_discord = models.CharField(max_length=200, blank=True, null=True)
    mod2_discord = models.CharField(max_length=200, blank=True, null=True)
    youtube_link = models.CharField(max_length=255, blank=True, null=True)
    speaker = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.start} {self.name}'


class Event(models.Model):
    name = models.CharField(max_length=500, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    start = models.TimeField(blank=False, null=False)
    mod1_discord = models.CharField(max_length=200, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    event_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.start} {self.name}'


class Shift(models.Model):
    location = models.CharField(max_length=500, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    start = models.TimeField(blank=False, null=False)
    end = models.TimeField(blank=False, null=False)
    discord_username = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.start} {self.name}'