# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='s_city',
            old_name='ProvinceID',
            new_name='Province',
        ),
        migrations.RenameField(
            model_name='s_district',
            old_name='CityID',
            new_name='City',
        ),
    ]
