# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ssp', '0010_auto_20161126_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculum',
            name='idioma',
            field=multiselectfield.db.fields.MultiSelectField(max_length=100, choices=[(b'espanol', b'espanol'), (b'ingles', b'ingles'), (b'japones', b'japones'), (b'ruso', b'ruso'), (b'aleman', b'aleman')]),
        ),
    ]
