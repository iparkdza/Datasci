# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20170116_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='score',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
