# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='views',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
