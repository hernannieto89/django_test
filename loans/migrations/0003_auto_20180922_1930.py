# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-22 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_remove_loanrequest_email_validation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanrequest',
            name='approval_status',
            field=models.NullBooleanField(default=False),
        ),
    ]