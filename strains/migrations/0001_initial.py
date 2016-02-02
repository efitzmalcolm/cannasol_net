# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.TextField(blank=True, unique=True)),
                ('logo', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='PotencyResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delta9_thc', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cbd', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cbn', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cbg', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cbc', models.DecimalField(decimal_places=2, max_digits=4)),
                ('delta8_thc', models.DecimalField(decimal_places=2, max_digits=4)),
                ('total_cannabinoids', models.DecimalField(decimal_places=2, max_digits=4)),
                ('total_thc', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'verbose_name': 'Potency Result',
                'verbose_name_plural': 'Potency Results',
            },
        ),
        migrations.CreateModel(
            name='qaSample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_name', models.CharField(max_length=50)),
                ('date_received', models.DateField()),
                ('date_reported', models.DateField()),
                ('sample_type', models.CharField(max_length=25)),
                ('lab_id', models.CharField(max_length=16)),
                ('sample_id', models.CharField(max_length=16, unique=True)),
                ('lot_id', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name': 'QA Sample',
                'verbose_name_plural': 'QA Samples',
            },
        ),
        migrations.CreateModel(
            name='Strain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strains.Brand')),
            ],
            options={
                'verbose_name': 'Strain',
                'verbose_name_plural': 'Strains',
            },
        ),
        migrations.CreateModel(
            name='Terpene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('short_desc', models.CharField(blank=True, max_length=250, null=True)),
                ('long_desc', models.TextField(blank=True, null=True)),
                ('aroma', models.CharField(blank=True, max_length=250, null=True)),
                ('flavor', models.CharField(blank=True, max_length=250, null=True)),
                ('effects', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Terpene',
                'verbose_name_plural': 'Terpenes',
            },
        ),
        migrations.CreateModel(
            name='TerpeneResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.DecimalField(decimal_places=2, max_digits=4)),
                ('qa_sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strains.qaSample')),
                ('terpene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strains.Terpene')),
            ],
            options={
                'verbose_name': 'Terpene Result',
                'verbose_name_plural': 'Terpene Results',
            },
        ),
        migrations.AddField(
            model_name='qasample',
            name='strain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strains.Strain'),
        ),
        migrations.AddField(
            model_name='potencyresult',
            name='qa_sample',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='strains.qaSample'),
        ),
        migrations.AlterUniqueTogether(
            name='terpeneresult',
            unique_together=set([('qa_sample', 'terpene')]),
        ),
    ]