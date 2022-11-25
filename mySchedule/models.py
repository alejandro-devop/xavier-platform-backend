from django.db import models
from django.contrib.auth.models import User
from activitiesApp.models import Activity


class Routine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=800, null=True, blank=True)
    initial_time = models.CharField(max_length=200)
    interval = models.IntegerField(default=15)
    is_monday = models.BooleanField(blank=True, null=True, default=False)
    is_tuesday = models.BooleanField(blank=True, null=True, default=False)
    is_wednesday = models.BooleanField(blank=True, null=True, default=False)
    is_thursday = models.BooleanField(blank=True, null=True, default=False)
    is_friday = models.BooleanField(blank=True, null=True, default=False)
    is_saturday = models.BooleanField(blank=True, null=True, default=False)
    is_sunday = models.BooleanField(blank=True, null=True, default=False)

    @staticmethod
    def get_object(user_id, item_id):
        try:
            return Routine.objects.get(id=item_id, user=user_id)
        except Routine.DoesNotExist:
            return None


class RoutineBlock(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    time_from = models.CharField(max_length=200, default="00:00:00")
    time_to = models.CharField(max_length=200, default="00:00:00")
    should_notify = models.BooleanField(blank=True, null=True, default=False)
    notify_time = models.IntegerField(default=10)

    @staticmethod
    def get_object(routine_id, item_id):
        try:
            return RoutineBlock.objects.get(id=item_id, routine=routine_id)
        except RoutineBlock.DoesNotExist:
            return None
