# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person_space', '0006_auto_20151016_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_org_certi',
            name='busi_lisence_photo',
            field=models.ImageField(upload_to=b'images/person/ico/', blank=True),
        ),
        migrations.AlterField(
            model_name='user_org_certi',
            name='org_photo',
            field=models.ImageField(upload_to=b'images/person/ico/', blank=True),
        ),
        migrations.AlterField(
            model_name='user_org_certi',
            name='tax_reg_photo',
            field=models.ImageField(upload_to=b'images/person/ico/', blank=True),
        ),
        migrations.AlterField(
            model_name='user_personal_certi',
            name='back_side_photo',
            field=models.ImageField(upload_to=b'images/person/ico/', blank=True),
        ),
        migrations.AlterField(
            model_name='user_personal_certi',
            name='forward_side_photo',
            field=models.ImageField(upload_to=b'images/person/ico/', blank=True),
        ),
    ]
