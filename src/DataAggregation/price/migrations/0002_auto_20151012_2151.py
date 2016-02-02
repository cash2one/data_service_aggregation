# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations #@UnusedImport


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_active_pack',
            name='service',
        ),
        migrations.RemoveField(
            model_name='service_price',
            name='service',
        ),
        migrations.RemoveField(
            model_name='service_sdk_pack',
            name='service',
        ),
        migrations.DeleteModel(
            name='Service_active_pack',
        ),
        migrations.DeleteModel(
            name='Service_price',
        ),
        migrations.DeleteModel(
            name='Service_sdk_pack',
        ),
    ]
