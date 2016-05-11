# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 23:13
from __future__ import unicode_literals

from django.db import migrations
from movie_data.models import Critic
from django.contrib.auth.models import User



def link_data(apps, schema_editor):

    for critic in Critic.objects.all():
        temp_id = critic.id+1
        print(type(critic.id))
        critic.user_id = User.objects.get(id=temp_id)

        critic.save()


class Migration(migrations.Migration):

    dependencies = [
        ('movie_data', '0008_critic_user'),
    ]

    operations = [
        migrations.RunPython(link_data)
    ]
