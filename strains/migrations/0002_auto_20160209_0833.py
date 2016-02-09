# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strains', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['name'], 'verbose_name': 'Brand', 'verbose_name_plural': 'Brands'},
        ),
        migrations.AlterModelOptions(
            name='strain',
            options={'ordering': ['name'], 'verbose_name': 'Strain', 'verbose_name_plural': 'Strains'},
        ),
        migrations.AlterModelOptions(
            name='terpene',
            options={'ordering': ['name'], 'verbose_name': 'Terpene', 'verbose_name_plural': 'Terpenes'},
        ),
        migrations.AlterField(
            model_name='qasample',
            name='strain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Samples', to='strains.Strain'),
        ),
    ]
