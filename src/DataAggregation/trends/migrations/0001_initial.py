# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('type_name', models.CharField(max_length=100)),
                ('info_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('visits', models.IntegerField(default=0, blank=True)),
            ],
            options={
                'ordering': ['-info_time'],
                'verbose_name': '\u52a8\u6001\u516c\u544a',
                'verbose_name_plural': '\u52a8\u6001\u516c\u544a',
            },
        ),
    ]
