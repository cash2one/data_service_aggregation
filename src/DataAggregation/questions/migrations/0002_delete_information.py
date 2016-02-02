# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations #@UnusedImport


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Information',
        ),
    ]
