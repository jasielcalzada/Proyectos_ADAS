# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssp', '0005_auto_20161125_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='estudiantess',
            field=models.ForeignKey(blank=True, to='ssp.Estudiante', null=True),
        ),
    ]
