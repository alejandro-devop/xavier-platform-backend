# Generated by Django 4.1 on 2022-08-07 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_verified', models.BooleanField(default=False)),
                ('verification_code', models.CharField(max_length=100)),
            ],
        ),
    ]
