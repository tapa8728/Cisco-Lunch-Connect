# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20150723_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manager_username', models.CharField(max_length=200)),
                ('intern_username', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('additionalinfo', models.CharField(max_length=200)),
                ('booked', models.BooleanField(default=b'false')),
            ],
        ),
    ]
