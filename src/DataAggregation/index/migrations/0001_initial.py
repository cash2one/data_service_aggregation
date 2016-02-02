# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search_Words',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=200)),
                ('visits', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['-visits'],
                'verbose_name': '\u70ed\u95e8\u641c\u7d22',
                'verbose_name_plural': '\u70ed\u95e8\u641c\u7d22',
            },
        ),
    ]
