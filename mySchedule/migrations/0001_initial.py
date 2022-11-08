# Generated by Django 4.1 on 2022-11-08 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activitiesApp', '0008_activitycategory_is_driving_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=800, null=True)),
                ('initial_time', models.CharField(max_length=200)),
                ('interval', models.IntegerField(default=15)),
                ('is_monday', models.BooleanField(blank=True, default=False, null=True)),
                ('is_tuesday', models.BooleanField(blank=True, default=False, null=True)),
                ('is_wednesday', models.BooleanField(blank=True, default=False, null=True)),
                ('is_thursday', models.BooleanField(blank=True, default=False, null=True)),
                ('is_friday', models.BooleanField(blank=True, default=False, null=True)),
                ('is_saturday', models.BooleanField(blank=True, default=False, null=True)),
                ('is_sunday', models.BooleanField(blank=True, default=False, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoutineBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_from', models.CharField(default='00:00:00', max_length=200)),
                ('time_to', models.CharField(default='00:00:00', max_length=200)),
                ('should_notify', models.BooleanField(blank=True, default=False, null=True)),
                ('notify_time', models.IntegerField(default=10)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activitiesApp.activity')),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mySchedule.routine')),
            ],
        ),
    ]
