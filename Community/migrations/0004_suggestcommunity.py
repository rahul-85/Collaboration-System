# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-02 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Community', '0003_communitygroups'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuggestCommunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('tag_line', models.CharField(max_length=500, null=True)),
                ('purpose', models.TextField()),
            ],
        ),
    ]
