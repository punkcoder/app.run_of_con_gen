# Generated by Django 3.2.6 on 2021-08-06 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runbook', '0003_talks_youtube_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='talks',
            name='speaker',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
