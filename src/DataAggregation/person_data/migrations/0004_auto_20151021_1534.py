# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person_data', '0003_auto_20151021_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data_service',
            name='service_name',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_data_service',
            name='call_times',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_data_service',
            name='left_times',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_data_service',
            name='total_times',
            field=models.IntegerField(default=0),
        ),
    ]
