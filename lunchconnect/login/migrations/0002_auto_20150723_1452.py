# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=20)),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('designation', models.CharField(max_length=40)),
                ('businessunit', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='password',
            name='username',
        ),
        migrations.DeleteModel(
            name='Password',
        ),
        migrations.DeleteModel(
            name='Username',
        ),
    ]
