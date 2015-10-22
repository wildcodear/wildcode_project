# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proform',
            name='client',
            field=models.ForeignKey(related_name='proforms_client', to='works.Client'),
        ),
        migrations.AddField(
            model_name='proform',
            name='company',
            field=models.ForeignKey(related_name='proforms_company', to='works.Company'),
        ),
    ]
