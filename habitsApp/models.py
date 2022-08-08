from django.db import models
from activitiesApp.models import Activity
from settingsApp.models import HabitMeasures
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

    @staticmethod
    def it_already_registered(name, user_id, item_id=None):
        if item_id is not None:
            items = HabitCategory\
                .objects\
                .filter(name__iexact=name, user=user_id)\
                .exclude(id=item_id)
        else:
            items = HabitCategory.objects.filter(name__iexact=name, user=user_id)
        return len(items) > 0

    @staticmethod
    def get_object(user_id, item_id):
        try:
            return HabitCategory.objects.get(id=item_id, user = user_id)
        except HabitCategory.DoesNotExist:
            return None

    def __str__(self):
        return self.name


class Habit(models.Model):
    """Model for the habits"""
    # Owner for the habit
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # Activity related to the habit
    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, blank=True, null=True)
    # Measure for the habit follow up
    measure = models.ForeignKey(HabitMeasures, on_delete=models.SET_NULL, blank=True, null=True)
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
    # If the habit is a timer
    is_timer = models.BooleanField(default=False)
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

    @staticmethod
    def already_exists(name, user_id, item_id=None):
        if item_id is not None:
            items = Habit\
                .objects\
                .filter(name__iexact=name, user=user_id)\
                .exclude(id=item_id)
        else:
            items = Habit.objects.filter(name__iexact=name, user=user_id)
        return len(items) > 0

    @staticmethod
    def get_object(user_id, item_id):
        try:
            return Habit.objects.get(id=item_id)
        except Habit.DoesNotExist:
            return None

    def __str__(self):
        return self.name
