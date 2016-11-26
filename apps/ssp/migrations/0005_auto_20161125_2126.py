# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssp', '0004_auto_20161125_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='empresa',
            field=models.ForeignKey(to='ssp.Empresa'),
        ),
    ]
