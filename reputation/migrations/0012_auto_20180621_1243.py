# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-21 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0011_defaultvalues_article_report_rejected'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultvalues',
            name='publisher_report',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='communityrep',
            name='rep',
            field=models.IntegerField(default=25),
        ),
        migrations.AlterField(
            model_name='defaultvalues',
            name='author_report',
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='defaultvalues',
            name='threshold_cadmin',
            field=models.PositiveIntegerField(default=3000),
        ),
        migrations.AlterField(
            model_name='defaultvalues',
            name='threshold_publisher',
            field=models.PositiveIntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='systemrep',
            name='sysrep',
            field=models.IntegerField(default=25),
        ),
    ]