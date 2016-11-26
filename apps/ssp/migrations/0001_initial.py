# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('nombre', models.CharField(max_length=64)),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('rfc', models.SlugField(serialize=False, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'perfil_empresa/', blank=True)),
                ('categoria', models.CharField(default=b'empresa', max_length=10, null=True)),
                ('user_perfil', models.OneToOneField(related_name='empresas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('nombre', models.CharField(max_length=64)),
                ('ncontrol', models.SlugField(serialize=False, primary_key=True)),
                ('carrera', models.CharField(default=b'No', max_length=64, choices=[(b'Ingenieria en sistemas computacionales', b'Ingenieria en sistemas computacionales'), (b'Ingenieria en TICS', b'Ingenieria en TICS'), (b'Ingenieria en informatica', b'Ingenieria en informatica')])),
                ('categoria', models.CharField(default=b'estudiante', max_length=10, null=True)),
                ('user_perfil', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
