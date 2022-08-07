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
