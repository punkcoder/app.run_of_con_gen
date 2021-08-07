import datetime

from django.shortcuts import render, HttpResponse
from .models import Talks, Event, Shift
import csv
import io
from datetime import time

# Create your views here.

def get_schedule(request):

    csvfile = io.StringIO()
    schedule = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL )

    for talk in Talks.objects.all():

        pretime = (talk.start.replace(hour=talk.start.hour - 1, minute=40))


        # set the pre time to -5 min
        pretime = (talk.start.replace(hour=talk.start.hour-1, minute=55))
        schedule.writerow([pretime,
                           talk.talk_mod1.discord,
                           "Send talk reminder in DEFCON - GENERAL",
                           f'"{talk.name}" by {talk.speaker} will be starting in 5 min! You can watch the talk at {talk.youtube_link} and head to #asv-talks-qa-text to discuss the talk and ask questions.',
                           ""])
        schedule.writerow([pretime,
                           talk.talk_mod1.discord,
                           "Send talk reminder in ASV - GENERAL",
                           f'"{talk.name}" by {talk.speaker} will be starting in 5 min! You can watch the talk at {talk.youtube_link} and head to #asv-talks-qa-text to discuss the talk and ask questions.',
                           ""])

        # set the pre time to -1 min
        pretime = (talk.start.replace(hour=talk.start.hour-1, minute=59))
        schedule.writerow([pretime,
                           talk.talk_mod1.discord,
                           "Welcome up coming talk in #asv-talks-qa-text",
                           f'"{talk.name}" by {talk.speaker} starts in 1 min! You can watch the talk here {talk.youtube_link}. Please feel free to use this space to ask text-based questions. The mods will collect the questions throughout the presentation and submit them to the Speaker to answer at the end of the talk.',
                           ""])

        # set at runtime
        schedule.writerow([
            talk.end,
            talk.talk_mod1.discord,
            f"Send speaker {talk.speaker} to the DEFCON Q&A voice room.  ",
            f'Test their A/V and your a/v  set all other people to mute',
            ""])

        # set the pre time to 5 min before end.
        new_min = (talk.end.minute - 5) % 60
        pretime = (talk.end.replace(minute=new_min))
        schedule.writerow([pretime,
                           talk.talk_mod1.discord,
                           "Send viewers to the DEFCON Q&A Voice room",
                           f'Thanks for attending "{talk.name}" by {talk.speaker.name}. Be sure to join us for the post-talk Q&A via #asv-talks-general. You can submit text-based questions about today’s talk and the Speaker will answer them verbally, so make sure your volume is up. This channel will remain open for discussion until our next talk begins. Feel free to continue the discussion in #asv-general-text.',
                           ""])

    for evnt in Event.objects.all():
        schedule.writerow([evnt.start,
                           evnt.event_mod1.discord,
                           "Send Event reminder in DEFCON - GENERAL",
                           f'{evnt.event_text}',
                           ""])
        schedule.writerow([evnt.start,
                           evnt.event_mod1.discord,
                           "Send Event reminder in ASV - GENERAL",
                           f'{evnt.event_text}',
                           ""])

    for sft in Shift.objects.all():
        pretime = (sft.start.replace(hour=sft.start.hour - 1, minute=45))
        schedule.writerow([
            pretime,
            sft.shift_worker.discord,
            f"Start Shift in {sft.location}",
            f"{sft.shift_worker.name} - {sft.shift_worker.email}",""
        ])
        schedule.writerow([
            sft.end,
            sft.shift_worker.discord,
            f"End Shift in {sft.location}",
            f"{sft.shift_worker.name} - {sft.shift_worker.email}", ""
        ])

    data = csvfile.getvalue()

    return HttpResponse(data, content_type="text/plain")
