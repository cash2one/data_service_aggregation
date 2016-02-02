# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person_space', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_secret',
            name='access_Key',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user_secret',
            name='open_id',
            field=models.CharField(max_length=200),
        ),
    ]
