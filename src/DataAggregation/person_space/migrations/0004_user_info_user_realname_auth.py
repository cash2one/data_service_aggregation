# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('person_space', '0003_auto_20151014_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile_no', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=100)),
                ('user_type', models.IntegerField()),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_realname_auth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('certi_type', models.IntegerField()),
                ('realname', models.CharField(max_length=100)),
                ('id_card_no', models.CharField(max_length=100)),
                ('forward_side_photo', models.BinaryField()),
                ('back_side_photo', models.BinaryField()),
                ('certi_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('certi_status', models.IntegerField()),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
