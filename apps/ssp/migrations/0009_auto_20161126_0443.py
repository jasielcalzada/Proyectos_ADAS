# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ssp', '0008_auto_20161126_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculum',
            name='idioma',
            field=multiselectfield.db.fields.MultiSelectField(max_length=5, choices=[(1, b'espanol'), (2, b'ingles'), (3, b'japones'), (4, b'ruso'), (5, b'aleman')]),
        ),
    ]
