# Generated by Django 4.1 on 2022-10-11 17:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soulmates', '0004_alter_visit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 17, 17, 52, 637072)),
        ),
    ]
