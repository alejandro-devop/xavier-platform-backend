from django.db import models
from django.contrib.auth.models import User
from activitiesApp.models import ActivityCategory


class Task(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(ActivityCategory, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    is_completed = models.BooleanField(default=False, blank=True, null=True)
    is_canceled = models.BooleanField(default=False, blank=True, null=True)
    date_line = models.DateField(blank=True, null=True)
    is_urgent = models.BooleanField(default=False, blank=True, null=True)
    priority = models.IntegerField(default=0, blank=True, null=True)
