# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hauntedhouse',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'ID')),
                ('area', models.CharField(max_length=2, null=True, db_column=b'Area', blank=True)),
                ('event', models.CharField(max_length=26, null=True, db_column=b'Event', blank=True)),
                ('location', models.CharField(max_length=23, null=True, db_column=b'Location', blank=True)),
                ('source', models.CharField(max_length=70, null=True, db_column=b'Source', blank=True)),
            ],
            options={
                'db_table': '00_HauntedHouse',
                'managed': False,
            },
        ),
    ]
