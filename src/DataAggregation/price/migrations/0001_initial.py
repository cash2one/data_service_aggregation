# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_active_pack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pack_name', models.CharField(max_length=500)),
                ('pack_desc', models.CharField(max_length=500)),
                ('pack_price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('pack_counts', models.IntegerField()),
                ('pack_effective_duration', models.CharField(max_length=100, blank=True)),
                ('status', models.IntegerField(choices=[(0, b'\xe5\x81\x9c\xe5\x94\xae'), (1, b'\xe7\x94\x9f\xe6\x95\x88'), (2, b'\xe5\xbe\x85\xe5\x94\xae')])),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('service', models.ForeignKey(related_name='rel_activepack', to='services.Service_base')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5957\u9910',
                'verbose_name_plural': '\u670d\u52a1\u5957\u9910',
            },
        ),
        migrations.CreateModel(
            name='Service_price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_free', models.BooleanField(default=True)),
                ('free_counts', models.IntegerField()),
                ('free_duration_unit', models.CharField(max_length=10, blank=True)),
                ('cost', models.DecimalField(max_digits=6, decimal_places=2)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('service', models.OneToOneField(related_name='rel_price', to='services.Service_base')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5b9a\u4ef7',
                'verbose_name_plural': '\u670d\u52a1\u5b9a\u4ef7',
            },
        ),
        migrations.CreateModel(
            name='Service_sdk_pack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pack_name', models.CharField(max_length=500)),
                ('pack_desc', models.CharField(max_length=500)),
                ('day_counts', models.IntegerField()),
                ('single_client_day_counts', models.IntegerField()),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('service', models.OneToOneField(related_name='rel_sdkpack', to='services.Service_base')),
            ],
            options={
                'verbose_name': 'SDK\u4f7f\u7528\u4f18\u60e0',
                'verbose_name_plural': 'SDK\u4f7f\u7528\u4f18\u60e0',
            },
        ),
    ]
