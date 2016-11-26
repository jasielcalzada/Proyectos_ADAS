# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ssp', '0006_proyecto_estudiantess'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tecnologias', models.TextField(max_length=500)),
                ('experiencia_profesional', models.TextField(max_length=1000)),
                ('idioma', multiselectfield.db.fields.MultiSelectField(max_length=9, choices=[(1, b'espanol'), (2, b'ingles'), (3, b'japones'), (4, b'ruso'), (5, b'aleman')])),
                ('fortaleza', models.CharField(max_length=64, choices=[(b'programacion modular', b'programacion modular'), (b'programacion WEB', b'programacion WEB'), (b'redes de compuradora', b'redes de computadora'), (b'administracion de base de datos', b'administracion de base de datos')])),
                ('done', models.BooleanField(default=False)),
                ('perfil', models.OneToOneField(related_name='more', to='ssp.Estudiante')),
            ],
        ),
    ]
