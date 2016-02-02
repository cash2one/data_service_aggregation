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
            name='Alipay_account_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=100)),
                ('account', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=1000)),
                ('score', models.IntegerField()),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': '\u6536\u6b3e\u652f\u4ed8\u5b9d\u8d26\u6237',
                'verbose_name_plural': '\u6536\u6b3e\u652f\u4ed8\u5b9d\u8d26\u6237',
            },
        ),
        migrations.CreateModel(
            name='Bank_account_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bank_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('account', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=1000)),
                ('score', models.IntegerField()),
            ],
            options={
                'verbose_name': '\u6536\u6b3e\u94f6\u884c\u8d26\u6237',
                'verbose_name_plural': '\u6536\u6b3e\u94f6\u884c\u8d26\u6237',
            },
        ),
        migrations.CreateModel(
            name='Charge_normal_logs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('charge_money', models.DecimalField(max_digits=10, decimal_places=2)),
                ('money_before', models.DecimalField(max_digits=10, decimal_places=2)),
                ('money_after', models.DecimalField(max_digits=10, decimal_places=2)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Charge_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=30)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Cost_normal_logs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cost_money', models.DecimalField(max_digits=10, decimal_places=2)),
                ('money_before', models.DecimalField(max_digits=10, decimal_places=2)),
                ('money_after', models.DecimalField(max_digits=10, decimal_places=2)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Cost_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=30)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DM_Charge_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=30)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DM_Cost_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=30)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User_account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('money', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_account_alarm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alarm_line', models.IntegerField(default=100)),
                ('alarm_status', models.IntegerField(default=0, choices=[(0, b'\xe5\x85\xb3\xe9\x97\xad'), (1, b'\xe5\xbc\x80\xe5\x90\xaf')])),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.ForeignKey(to='person_finance.User_account')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('discount', models.DecimalField(max_digits=2, decimal_places=1)),
                ('limit_date', models.DateField(default=django.utils.timezone.now)),
                ('limit_times', models.IntegerField()),
                ('used', models.IntegerField(default=0, choices=[(0, b'\xe6\x9c\xaa\xe4\xbd\xbf\xe7\x94\xa8'), (1, b'\xe5\xb7\xb2\xe4\xbd\xbf\xe7\x94\xa8')])),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_DM_account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coins', models.IntegerField(default=0)),
                ('free_coins', models.IntegerField(default=0)),
                ('pay_coins', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_DM_charge_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coins', models.IntegerField(default=0)),
                ('coins_before', models.IntegerField(default=0)),
                ('coins_after', models.IntegerField(default=0)),
                ('free_coins_before', models.IntegerField(default=0)),
                ('free_coins_after', models.IntegerField(default=0)),
                ('pay_coins_before', models.IntegerField(default=0)),
                ('pay_coins_after', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('charge_type', models.ForeignKey(default=1, to='person_finance.DM_Charge_type')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_DM_cost_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coins', models.IntegerField(default=0)),
                ('coins_before', models.IntegerField(default=0)),
                ('coins_after', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('cost_type', models.ForeignKey(default=1, to='person_finance.DM_Cost_type')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cost_normal_logs',
            name='account',
            field=models.ForeignKey(to='person_finance.User_account'),
        ),
        migrations.AddField(
            model_name='cost_normal_logs',
            name='cost_type',
            field=models.ForeignKey(default=1, to='person_finance.Cost_type'),
        ),
        migrations.AddField(
            model_name='cost_normal_logs',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='charge_normal_logs',
            name='account',
            field=models.ForeignKey(to='person_finance.User_account'),
        ),
        migrations.AddField(
            model_name='charge_normal_logs',
            name='charge_type',
            field=models.ForeignKey(default=1, to='person_finance.Charge_type'),
        ),
        migrations.AddField(
            model_name='charge_normal_logs',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
