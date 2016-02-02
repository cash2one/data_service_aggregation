# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('person_data', '0002_user_data_service_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='IP_white_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allow_ips', models.TextField()),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='user_data_service',
            name='status',
            field=models.IntegerField(choices=[(0, b'\xe6\x9c\xaa\xe5\xae\xa1\xe6\xa0\xb8'), (1, b'\xe5\xae\xa1\xe6\xa0\xb8\xe4\xb8\xad'), (2, b'\xe5\xae\xa1\xe6\xa0\xb8\xe9\x80\x9a\xe8\xbf\x87'), (3, b'\xe5\xae\xa1\xe6\xa0\xb8\xe9\xa9\xb3\xe5\x9b\x9e')]),
        ),
        migrations.AddField(
            model_name='ip_white_list',
            name='user_service',
            field=models.OneToOneField(to='person_data.User_data_service'),
        ),
    ]
