# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20170116_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='score',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
