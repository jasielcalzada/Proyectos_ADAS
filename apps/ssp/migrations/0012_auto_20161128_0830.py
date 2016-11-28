# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssp', '0011_auto_20161126_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='empresa',
            field=models.ForeignKey(related_name='em', to='ssp.Empresa'),
        ),
    ]
