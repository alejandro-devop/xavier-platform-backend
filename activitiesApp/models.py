from django.db import models
from django.contrib.auth.models import User


class ActivityCategory(models.Model):
    """Model for the categories for each activity"""
    # Owner for the activity category
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
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

    @staticmethod
    def it_already_registered(name, user_id, item_id=None):
        if item_id is not None:
            items = ActivityCategory\
                .objects\
                .filter(name__iexact=name, user=user_id)\
                .exclude(id=item_id)
        else:
            items = ActivityCategory.objects.filter(name__iexact=name, user=user_id)
        return len(items) > 0

    @staticmethod
    def get_object(user_id, item_id):
        try:
            return ActivityCategory.objects.get(id=item_id, user=user_id)
        except ActivityCategory.DoesNotExist:
            return None

    def __str__(self):
        """Override when printing the object"""
        return self.name


class Activity(models.Model):
    """Model for the activities"""
    # Owner for the activity
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
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
