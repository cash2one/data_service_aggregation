# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Common_http_demo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('hyperlink', models.CharField(max_length=500)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
            ],
            options={
                'verbose_name': 'Http\u901a\u7528\u793a\u4f8b',
                'verbose_name_plural': 'Http\u901a\u7528\u793a\u4f8b',
            },
        ),
        migrations.CreateModel(
            name='Service_api',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=500)),
                ('format', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
            ],
            options={
                'verbose_name': 'api\u8be6\u60c5',
                'verbose_name_plural': 'api\u8be6\u60c5',
            },
        ),
        migrations.CreateModel(
            name='Service_base',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serve_name', models.CharField(max_length=200)),
                ('serve_desc', models.CharField(max_length=1000)),
                ('serve_logo', models.ImageField(upload_to=b'images/service/ico/', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u57fa\u7840\u4fe1\u606f',
                'verbose_name_plural': '\u670d\u52a1\u57fa\u7840\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Service_category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=100)),
                ('parent_category_id', models.IntegerField(default=0, blank=True)),
                ('serve_cate_logo', models.ImageField(upload_to=b'images/ico/', blank=True)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('order_num', models.IntegerField()),
            ],
            options={
                'ordering': ['order_num'],
                'verbose_name': '\u670d\u52a1\u7c7b\u522b',
                'verbose_name_plural': '\u670d\u52a1\u7c7b\u522b',
            },
        ),
        migrations.CreateModel(
            name='Service_contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('support_team', models.CharField(max_length=500)),
                ('QQ_group', models.CharField(max_length=20)),
                ('phone_No', models.CharField(max_length=20)),
                ('QQ_online_contact', models.CharField(max_length=100)),
                ('QQ_cooperator', models.CharField(max_length=100)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('service', models.OneToOneField(to='services.Service_base')),
            ],
            options={
                'verbose_name': '\u8054\u7cfb\u5f00\u53d1\u5546',
                'verbose_name_plural': '\u8054\u7cfb\u5f00\u53d1\u5546',
            },
        ),
        migrations.CreateModel(
            name='Service_error_code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('error_code', models.CharField(max_length=100)),
                ('error_name', models.CharField(max_length=1000)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
            ],
            options={
                'verbose_name': '\u9519\u8bef\u4ee3\u7801',
                'verbose_name_plural': '\u9519\u8bef\u4ee3\u7801',
            },
        ),
        migrations.CreateModel(
            name='Service_error_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('error_type_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u9519\u8bef\u7c7b\u578b',
                'verbose_name_plural': '\u670d\u52a1\u9519\u8bef\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='Service_invoke_demo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('hyperlink', models.CharField(max_length=500)),
                ('provider', models.CharField(max_length=200)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('service', models.ForeignKey(to='services.Service_base')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u8c03\u7528\u793a\u4f8b',
                'verbose_name_plural': '\u670d\u52a1\u8c03\u7528\u793a\u4f8b',
            },
        ),
        migrations.CreateModel(
            name='Service_others',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=100)),
                ('detail', models.TextField(max_length=1000)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('service', models.ForeignKey(to='services.Service_base')),
            ],
            options={
                'verbose_name': '\u5176\u4ed6\u670d\u52a1\u76f8\u5173',
                'verbose_name_plural': '\u5176\u4ed6\u670d\u52a1\u76f8\u5173',
            },
        ),
        migrations.CreateModel(
            name='Service_protocol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('protocol_name', models.CharField(max_length=200)),
                ('support_operate', models.CharField(max_length=200, blank=True)),
            ],
            options={
                'verbose_name': '\u534f\u8bae',
                'verbose_name_plural': '\u534f\u8bae',
            },
        ),
        migrations.CreateModel(
            name='Service_provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provider_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': '\u6570\u636e\u4f9b\u5e94\u5546',
                'verbose_name_plural': '\u6570\u636e\u4f9b\u5e94\u5546',
            },
        ),
        migrations.CreateModel(
            name='Service_reqDemo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('demo_format', models.CharField(max_length=100)),
                ('demo_str', models.TextField(max_length=1000)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('service', models.ForeignKey(to='services.Service_base')),
            ],
            options={
                'verbose_name': '\u8bf7\u6c42\u793a\u4f8b',
                'verbose_name_plural': '\u8bf7\u6c42\u793a\u4f8b',
            },
        ),
        migrations.CreateModel(
            name='Service_reqField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_name', models.CharField(max_length=100)),
                ('field_type', models.IntegerField(choices=[(1, b'\xe5\xad\x97\xe7\xac\xa6\xe5\x9e\x8b'), (2, b'\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2'), (3, b'\xe6\x95\xb4\xe6\x95\xb0\xe5\x9e\x8b'), (4, b'\xe5\xb0\x8f\xe6\x95\xb0\xe5\x9e\x8b'), (5, b'\xe6\x97\xa5\xe6\x9c\x9f\xe5\x9e\x8b'), (6, b'\xe6\x97\xa5\xe6\x9c\x9f\xe6\x97\xb6\xe9\x97\xb4\xe5\x9e\x8b'), (7, b'\xe6\x96\x87\xe4\xbb\xb6\xe5\x9e\x8b')])),
                ('required', models.IntegerField(choices=[(0, b'\xe5\x90\xa6'), (1, b'\xe6\x98\xaf')])),
                ('description', models.CharField(max_length=1000)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('service', models.ForeignKey(to='services.Service_base')),
            ],
            options={
                'verbose_name': '\u4f20\u53c2\u8bbe\u7f6e',
                'verbose_name_plural': '\u4f20\u53c2\u8bbe\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='Service_respDemo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('demo_format', models.CharField(max_length=100)),
                ('demo_str', models.TextField(max_length=2000)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('service', models.ForeignKey(to='services.Service_base')),
            ],
            options={
                'verbose_name': '\u8fd4\u56de\u793a\u4f8b',
                'verbose_name_plural': '\u8fd4\u56de\u793a\u4f8b',
            },
        ),
        migrations.CreateModel(
            name='Service_respField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_name', models.CharField(max_length=100)),
                ('field_type', models.IntegerField(choices=[(1, b'\xe5\xad\x97\xe7\xac\xa6\xe5\x9e\x8b'), (2, b'\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2'), (3, b'\xe6\x95\xb4\xe6\x95\xb0\xe5\x9e\x8b'), (4, b'\xe5\xb0\x8f\xe6\x95\xb0\xe5\x9e\x8b'), (5, b'\xe6\x97\xa5\xe6\x9c\x9f\xe5\x9e\x8b'), (6, b'\xe6\x97\xa5\xe6\x9c\x9f\xe6\x97\xb6\xe9\x97\xb4\xe5\x9e\x8b'), (7, b'\xe6\x96\x87\xe4\xbb\xb6\xe5\x9e\x8b')])),
                ('description', models.CharField(max_length=1000)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('service', models.ForeignKey(to='services.Service_base')),
            ],
            options={
                'verbose_name': '\u8fd4\u56de\u503c\u8bbe\u7f6e',
                'verbose_name_plural': '\u8fd4\u56de\u503c\u8bbe\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='Service_score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scores', models.DecimalField(max_digits=2, decimal_places=1)),
                ('contact_apps', models.IntegerField()),
                ('visits', models.IntegerField()),
                ('service', models.OneToOneField(related_name='rel_score', to='services.Service_base')),
            ],
            options={
                'verbose_name': '\u79ef\u5206\u548c\u8bbf\u95ee\u91cf',
                'verbose_name_plural': '\u79ef\u5206\u548c\u8bbf\u95ee\u91cf',
            },
        ),
        migrations.CreateModel(
            name='Service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u72b6\u6001',
                'verbose_name_plural': '\u670d\u52a1\u72b6\u6001',
            },
        ),
        migrations.CreateModel(
            name='Service_Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=b'100')),
                ('tag_color', models.IntegerField()),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u6807\u7b7e',
                'verbose_name_plural': '\u670d\u52a1\u6807\u7b7e',
            },
        ),
        migrations.CreateModel(
            name='Service_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=100)),
                ('parent_type_id', models.IntegerField(default=0, blank=True)),
                ('serve_type_logo', models.ImageField(upload_to=b'images/ico/', blank=True)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('order_num', models.IntegerField()),
                ('category', models.ForeignKey(to='services.Service_category')),
            ],
            options={
                'ordering': ['order_num'],
                'verbose_name': '\u670d\u52a1\u7c7b\u578b',
                'verbose_name_plural': '\u670d\u52a1\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='Service_upgrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upgrade_contents', models.CharField(max_length=500)),
                ('upgrade_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('service', models.ForeignKey(to='services.Service_base')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u66f4\u65b0\u8bb0\u5f55',
                'verbose_name_plural': '\u670d\u52a1\u66f4\u65b0\u8bb0\u5f55',
            },
        ),
        migrations.AddField(
            model_name='service_error_code',
            name='error_type',
            field=models.ForeignKey(to='services.Service_error_type'),
        ),
        migrations.AddField(
            model_name='service_error_code',
            name='service',
            field=models.ForeignKey(to='services.Service_base'),
        ),
        migrations.AddField(
            model_name='service_base',
            name='protocol',
            field=models.ForeignKey(to='services.Service_protocol'),
        ),
        migrations.AddField(
            model_name='service_base',
            name='provider',
            field=models.ForeignKey(to='services.Service_provider'),
        ),
        migrations.AddField(
            model_name='service_base',
            name='serve_type',
            field=models.ForeignKey(to='services.Service_type'),
        ),
        migrations.AddField(
            model_name='service_base',
            name='status',
            field=models.ForeignKey(to='services.Service_status'),
        ),
        migrations.AddField(
            model_name='service_base',
            name='tags',
            field=models.ManyToManyField(to='services.Service_Tag', blank=True),
        ),
        migrations.AddField(
            model_name='service_api',
            name='service',
            field=models.OneToOneField(related_name='rel_api', to='services.Service_base'),
        ),
    ]
