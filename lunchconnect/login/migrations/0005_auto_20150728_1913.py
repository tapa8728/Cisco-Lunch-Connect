# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20150728_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=b'2009-10-03'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='endtime',
            field=models.TimeField(default=b'12:00'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='starttime',
            field=models.TimeField(default=b'12:00'),
        ),
    ]
