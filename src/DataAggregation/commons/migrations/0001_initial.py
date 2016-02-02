# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='S_City',
            fields=[
                ('CityID', models.AutoField(serialize=False, verbose_name=b'CityID', primary_key=True)),
                ('CityName', models.CharField(max_length=100)),
                ('ZipCode', models.CharField(max_length=100)),
                ('DateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('DateUpdated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 's_city',
                'verbose_name': '\u5e02',
                'verbose_name_plural': '\u5e02',
            },
        ),
        migrations.CreateModel(
            name='S_District',
            fields=[
                ('DistrictID', models.AutoField(serialize=False, verbose_name=b'DistrictID', primary_key=True)),
                ('DistrictName', models.CharField(max_length=100)),
                ('DateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('DateUpdated', models.DateTimeField(default=django.utils.timezone.now)),
                ('CityID', models.ForeignKey(to='commons.S_City', db_column=b'CityID')),
            ],
            options={
                'db_table': 's_district',
                'verbose_name': '\u533a',
                'verbose_name_plural': '\u533a',
            },
        ),
        migrations.CreateModel(
            name='S_Province',
            fields=[
                ('ProvinceID', models.AutoField(serialize=False, verbose_name=b'ProvinceID', primary_key=True)),
                ('ProvinceName', models.CharField(max_length=100)),
                ('DateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('DateUpdated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 's_province',
                'verbose_name': '\u7701\u4efd',
                'verbose_name_plural': '\u7701\u4efd',
            },
        ),
        migrations.AddField(
            model_name='s_city',
            name='ProvinceID',
            field=models.ForeignKey(to='commons.S_Province', db_column=b'ProvinceID'),
        ),
    ]
