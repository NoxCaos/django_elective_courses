# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-13 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElectiveCourses', '0003_course_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(to='ElectiveCourses.Student'),
        ),
    ]
