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

    @staticmethod
    def is_already_registered(name, user_id, item_id=None):
        if item_id is not None:
            items = Task \
                .objects \
                .filter(title__iexact=name, user=user_id) \
                .exclude(id=item_id)
        else:
            items = Task.objects.filter(title__iexact=name, user=user_id)
        print(items)
        return len(items) > 0

    @staticmethod
    def get_object(user_id, item_id):
        try:
            return Task.objects.get(id=item_id, user=user_id)
        except Task.DoesNotExist:
            return None

    def __str__(self):
        return self.title