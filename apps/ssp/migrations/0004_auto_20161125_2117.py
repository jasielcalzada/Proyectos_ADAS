# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssp', '0003_proyecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='aprovado',
            field=models.CharField(default=b'en proceso', max_length=44, choices=[(b'aprovado', b'aprovado'), (b'rechasado', b'rechasado'), (b'en proceso', b'en proceso')]),
        ),
    ]
