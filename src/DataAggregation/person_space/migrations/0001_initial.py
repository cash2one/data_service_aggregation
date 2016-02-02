# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Secret',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('open_id', models.CharField(max_length=32)),
                ('access_Key', models.CharField(max_length=32)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u79d8\u94a5',
                'verbose_name_plural': '\u7528\u6237\u79d8\u94a5',
            },
        ),
    ]
