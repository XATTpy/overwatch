# Generated by Django 2.1.2 on 2018-12-07 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_video_hero_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='Hero_name',
            new_name='Video_hero',
        ),
    ]