# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20151022_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proform',
            name='payment_conditions',
            field=models.CharField(max_length=100, choices=[(b'cash', 'Cash'), (b'credit_card', 'Credit card'), (b'negotiable', 'Negotiable'), (b'transfer', 'Transfer')]),
        ),
    ]
