# Generated by Django 4.1 on 2022-11-01 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activitiesApp', '0008_activitycategory_is_driving_and_more'),
        ('lifeGoals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activitiesApp.activitycategory'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='description',
            field=models.TextField(blank=True, max_length=800, null=True),
        ),
    ]