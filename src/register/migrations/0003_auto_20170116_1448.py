# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_register_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='score',
            field=models.IntegerField(max_length=10),
        ),
    ]
