# Generated by Django 4.1 on 2022-10-27 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('habitsApp', '0002_habit_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='daily_goal',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='habit',
            name='is_decremental',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='habit',
            name='is_incremental',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.CreateModel(
            name='HabitType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_number_goal', models.BooleanField(blank=True, default=False, null=True)),
                ('is_quantity_goal', models.BooleanField(blank=True, default=False, null=True)),
                ('is_duration_goal', models.BooleanField(blank=True, default=False, null=True)),
                ('is_distance_goal', models.BooleanField(blank=True, default=False, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='habit',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habitsApp.habittype'),
        ),
    ]