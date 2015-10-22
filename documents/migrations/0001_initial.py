# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expire_on', models.DateTimeField()),
                ('payment_conditions', models.CharField(max_length=100)),
                ('total_to_pay', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime_in', models.DateTimeField()),
                ('machine_data', models.TextField()),
                ('problem', models.TextField()),
                ('diagnosis', models.TextField()),
                ('treatment', models.TextField()),
                ('observations', models.TextField(null=True, blank=True)),
                ('suggestions', models.TextField(null=True, blank=True)),
                ('datetime_out', models.DateTimeField()),
                ('technical', models.CharField(max_length=100)),
            ],
        ),
    ]
