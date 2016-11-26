# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssp', '0002_remove_empresa_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.SlugField(max_length=64)),
                ('descripcion', models.CharField(max_length=240)),
                ('fecha_publicacion', models.DateField()),
                ('perfil_proyecto', models.TextField(max_length=64)),
                ('mostrar', models.BooleanField(default=False)),
                ('categoria', models.CharField(default=False, max_length=124, choices=[(b'programacion modular', b'programacion modular'), (b'programacion WEB', b'programacion WEB'), (b'redes de compuradora', b'redes de computadora'), (b'administracion de base de datos', b'administracion de base de datos'), (b'prueva', b'prueva')])),
                ('selecionar', models.BooleanField(default=False)),
                ('aprovado', models.CharField(default=b'no', max_length=44, choices=[(b'aprovado', b'aprovado'), (b'rechasado', b'rechasado')])),
                ('empresa', models.OneToOneField(to='ssp.Empresa')),
            ],
        ),
    ]
