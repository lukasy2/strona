# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-16 12:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artykuly', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Kurs', 'verbose_name_plural': 'Kursy'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategoria', 'verbose_name_plural': 'Kategorie'},
        ),
        migrations.AlterModelOptions(
            name='lekcja',
            options={'verbose_name': 'Lekcja', 'verbose_name_plural': 'Lekcje'},
        ),
    ]
