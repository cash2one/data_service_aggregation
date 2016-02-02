# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data_service',
            name='status',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
