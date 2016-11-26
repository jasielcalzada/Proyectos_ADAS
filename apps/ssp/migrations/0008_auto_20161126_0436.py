# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ssp', '0007_curriculum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculum',
            name='perfil',
            field=models.OneToOneField(related_name='more', to=settings.AUTH_USER_MODEL),
        ),
    ]
