# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('person_space', '0005_user_realname_auth_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Org_Certi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('busi_lisence_no', models.CharField(max_length=100)),
                ('busi_lisence_photo', models.BinaryField()),
                ('tax_reg_no', models.CharField(max_length=100)),
                ('tax_reg_photo', models.BinaryField()),
                ('org_no', models.CharField(max_length=100)),
                ('org_photo', models.BinaryField()),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_phone', models.CharField(max_length=100)),
                ('certi_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('certi_status', models.IntegerField()),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Personal_Certi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('realname', models.CharField(max_length=100)),
                ('id_card_no', models.CharField(max_length=100)),
                ('forward_side_photo', models.BinaryField()),
                ('back_side_photo', models.BinaryField()),
                ('certi_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('certi_status', models.IntegerField()),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_realname_auth',
            name='user',
        ),
        migrations.DeleteModel(
            name='User_realname_auth',
        ),
    ]
