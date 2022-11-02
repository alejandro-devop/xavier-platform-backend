from django.db import models
from django.contrib.auth.models import User
from activitiesApp.models import ActivityCategory


# Create your models here.
class Goal(models.Model):
    category = models.ForeignKey(ActivityCategory, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=800, null=True, blank=True)
    is_accomplished = models.BooleanField(null=True, blank=True, default=False)
    dead_line_date = models.DateField(null=True, blank=True)

    @staticmethod
    def is_already_registered(name, user_id, item_id=None):
        if item_id is not None:
            items = Goal\
                .objects\
                .filter(name__iexact=name, user=user_id)\
                .exclude(id=item_id)
        else:
            items = Goal.objects.filter(name__iexact=name, user=user_id)
        return len(items) > 0

    @staticmethod
    def get_object(user_id, item_id):
        try:
            return Goal.objects.get(id=item_id, user=user_id)
        except Goal.DoesNotExist:
            return None


class GoalReason(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    Goal = models.ForeignKey(Goal, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=800)
    is_positive = models.BooleanField(null=True, blank=True, default=False)
    is_negative = models.BooleanField(null=True, blank=True, default=False)


class GoalObjetive(models.Model):
    name = models.CharField(max_length=200)
    Goal = models.ForeignKey(Goal, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=800)
    is_accomplished = models.BooleanField(null=True, blank=True, default=False)
