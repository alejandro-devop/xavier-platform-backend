from django.db import models
from activitiesApp.models import Activity
from django.contrib.auth.models import User


class HabitCategory(models.Model):
    """Model for the habit categories"""
    # Owner for the habit category
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Name for the habit category
    name = models.CharField(max_length=200)
    # Brief description for the habit category
    description = models.TextField(max_length=800)
    # A fontawesome icon name
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Habit(models.Model):
    """Model for the habits"""
    # Owner for the habit
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Activity related to the habit
    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, blank=True, null=True)
    # Name for the habit
    name = models.CharField(max_length=200)
    # Brief description for the habit
    description = models.TextField(max_length=800)
    # If the habit should be avoided
    should_avoid = models.BooleanField(default=False)
    # If the habit should be kept
    should_keep = models.BooleanField(default=False)
    # If the habit follow up is a counter
    is_counter = models.BooleanField(default=False)
    # The estimated duration for the habit (number of steps to success)
    days = models.IntegerField(default=90)
    # The current habit streak, it will be reset when no accomplished
    streak = models.IntegerField(default=0)
    # The maximum accomplished streak
    max_streak = models.IntegerField(default=0)
    # Started date for the habit
    start_date = models.DateField()
    # Estimated finalization for the habit, is the sum of the started date plus dayss
    end_date = models.DateField()

    def __str__(self):
        return self.name
