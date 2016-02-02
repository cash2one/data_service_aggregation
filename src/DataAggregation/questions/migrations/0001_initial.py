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
            name='Anwser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=1000)),
                ('anwser_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u56de\u7b54',
                'verbose_name_plural': '\u56de\u7b54',
            },
        ),
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
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('quest_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('lastest_anwser_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('visits', models.IntegerField(default=0, blank=True)),
            ],
            options={
                'ordering': ['-lastest_anwser_time'],
                'verbose_name': '\u95ee\u9898',
                'verbose_name_plural': '\u95ee\u9898',
            },
        ),
        migrations.CreateModel(
            name='Question_Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=20)),
                ('visits', models.IntegerField(default=0, blank=True)),
            ],
            options={
                'verbose_name': '\u95ee\u9898\u6807\u7b7e',
                'verbose_name_plural': '\u95ee\u9898\u6807\u7b7e',
            },
        ),
        migrations.CreateModel(
            name='Question_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '\u95ee\u9898\u5206\u7c7b',
                'verbose_name_plural': '\u95ee\u9898\u5206\u7c7b',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='questions.Question_Tag'),
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.ForeignKey(to='questions.Question_Type'),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='anwser',
            name='question',
            field=models.ForeignKey(to='questions.Question'),
        ),
        migrations.AddField(
            model_name='anwser',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
