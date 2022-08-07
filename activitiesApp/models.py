from django.db import models


class ActivityCategory(models.Model):
    """Model for the categories for each activity"""
    # Name for the category
    name = models.CharField(max_length=200)
    # A color for the category activities
    color = models.CharField(max_length=100)
    # Brief description for the category
    description = models.TextField(max_length=800)
    # A fontawesome icon name
    icon = models.CharField(max_length=200)
    # If the category is for rest activities
    is_rest = models.BooleanField(default=False)
    # If the category is for working activities
    is_work = models.BooleanField(default=False)
    # If the category is for learning activities
    is_learning = models.BooleanField(default=False)
    # If the category is for self-care activities
    is_self_care = models.BooleanField(default=False)
    # If the category is for exercise activities
    is_exercise = models.BooleanField(default=False)

    def __str__(self):
        """Override when printing the object"""
        return self.name


class Activity(models.Model):
    """Model for the activities"""
    # Category associated to the activity
    category = models.ForeignKey(ActivityCategory, on_delete=models.CASCADE)
    # A color to distinguish the activity on reports
    color = models.CharField(max_length=100)
    # The name for the activity
    name = models.CharField(max_length=200)
    # A brief description for the activity
    description = models.TextField(max_length=800)

    def __str__(self):
        return self.category.name + ": " + self.name
