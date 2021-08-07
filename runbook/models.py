from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=500,blank=False, null=False)
    discord = models.CharField(max_length=500,blank=True, null=True)
    email = models.CharField(max_length=500,blank=True, null=True)
    is_volunteer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_speaker = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.discord}'


class Talks(models.Model):
    name = models.CharField(max_length=500,blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    start = models.TimeField(blank=False, null=False)
    end = models.TimeField(blank=False, null=False)
    talk_mod1 = models.ForeignKey(Person, on_delete=models.DO_NOTHING,related_name= "talk_mod1", null=True, blank=True)
    talk_mod2 = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name= "talk_mod2", null=True, blank=True)
    youtube_link = models.CharField(max_length=255, blank=True, null=True)
    speaker = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name="talk_speaker")

    def __str__(self):
        return f'{self.date} {self.start} {self.name}'

    class Meta:
        verbose_name_plural = 'talks'


class Event(models.Model):
    name = models.CharField(max_length=500, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    start = models.TimeField(blank=False, null=False)
    event_mod1 = models.ForeignKey(Person, on_delete=models.DO_NOTHING,related_name= "event_mod1", null=True, blank=True)
    event_mod2 = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name="event_mod2", null=True, blank=True)
    host = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name="host", null=True, blank=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    event_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.date} {self.start} {self.name}'


class Location(models.Model):
    name = models.CharField(max_length=500, blank=False, null=False)

    def __str__(self):
        return f'{self.name}'


class Shift(models.Model):
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    date = models.DateField(blank=False, null=False)
    start = models.TimeField(blank=False, null=False)
    end = models.TimeField(blank=False, null=False)
    shift_worker = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name="worker", null=True, blank=True)

    def __str__(self):
        return f'{self.date} {self.start}'