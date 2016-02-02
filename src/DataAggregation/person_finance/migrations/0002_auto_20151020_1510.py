# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person_finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='charge_normal_logs',
            name='number_of_pack',
            field=models.IntegerField(default=1, blank=True),
        ),
        migrations.AddField(
            model_name='charge_normal_logs',
            name='serve_base_id',
            field=models.IntegerField(default=None, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='charge_normal_logs',
            name='serve_pack_id',
            field=models.IntegerField(default=None, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cost_normal_logs',
            name='cost_type',
            field=models.ForeignKey(default=2, to='person_finance.Cost_type'),
        ),
    ]
