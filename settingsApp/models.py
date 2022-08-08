from django.db import models
from django.contrib.auth.models import User


class HabitMeasures(models.Model):
    """Model for measuring the habits followup"""
    # User owner for the measure
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # Name for the measure
    name = models.CharField(max_length=100)
    # An abbreviation for the measure.
    abbreviation = models.CharField(max_length=100)

    @staticmethod
    def already_registered(name, user_id, item_id=None):
        if item_id is not None:
            items = HabitMeasures\
                .objects\
                .filter(name__iexact=name, user=user_id)\
                .exclude(id=item_id)
        else:
            items = HabitMeasures.objects.filter(name__iexact=name, user=user_id)
        return len(items) > 0

    @staticmethod
    def get_object(user_id, item_id):
        try:
            return HabitMeasures.objects.get(id=item_id, user=user_id)
        except HabitMeasures.DoesNotExist:
            return None
