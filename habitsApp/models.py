from django.db import models


class HabitCategory(models.Model):
    """Model for the habit categories"""
    # Name for the habit category
    name = models.CharField(max_length=200)
    # Brief description for the habit category
    description = models.TextField(max_length=800)
    # A fontawesome icon name
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name
