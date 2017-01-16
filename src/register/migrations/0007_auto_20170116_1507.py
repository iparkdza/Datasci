# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_auto_20170116_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='score',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
