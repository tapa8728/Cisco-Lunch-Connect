# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='additionalinfo',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='booked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='intern_username',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='location',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
