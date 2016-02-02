# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageBoard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11, blank=True)),
                ('messagecontent', models.TextField(max_length=1000)),
                ('msg_time', models.DateTimeField(default=django.utils.timezone.now, null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u7559\u8a00\u677f',
                'verbose_name_plural': '\u7559\u8a00\u677f',
            },
        ),
    ]
