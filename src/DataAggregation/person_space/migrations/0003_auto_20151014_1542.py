# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person_space', '0002_auto_20151014_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_secret',
            old_name='user_id',
            new_name='user',
        ),
    ]
