# Generated by Django 4.1 on 2022-08-07 20:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
                ('times_visited', models.IntegerField(default=0)),
                ('photo_url', models.TextField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 8, 7, 20, 22, 37, 794777))),
                ('place_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='soulmates.place')),
            ],
        ),
        migrations.CreateModel(
            name='VisitComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=800)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('visit_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='soulmates.visit')),
            ],
        ),
        migrations.CreateModel(
            name='SoulMate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_confirmed', models.BooleanField(default=False)),
                ('soulmate_receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='soulmate_receiver', to=settings.AUTH_USER_MODEL)),
                ('soulmate_sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='soulmate_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_url', models.TextField(max_length=800)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('visit_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='soulmates.visit')),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='soulmate_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='soulmates.soulmate'),
        ),
    ]