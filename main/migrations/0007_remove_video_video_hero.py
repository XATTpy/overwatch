# Generated by Django 2.1.2 on 2018-12-07 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_video_video_hero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='Video_Hero',
        ),
    ]
