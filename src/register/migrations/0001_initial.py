# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100, null=True, blank=True)),
                ('password', models.CharField(max_length=100, null=True, blank=True)),
                ('firstName', models.CharField(max_length=100, null=True, blank=True)),
                ('lastName', models.CharField(max_length=100, null=True, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('birthdate', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(default=b'M', max_length=1, null=True, choices=[(b'M', b'Male'), (b'F', b'Female')])),
            ],
        ),
    ]
