import datetime
from django.db import models
from django.contrib.auth.models import User


class SoulMate(models.Model):
    soulmate_left = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    soulmate_right = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    is_confirmed = models.BooleanField(default=False)


class Place(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    times_visited = models.IntegerField(default=0)
    soulmate_id = models.ForeignKey(SoulMate, on_delete=models.CASCADE, blank=True, null=True)
    photo_url = models.TextField(max_length=800)


class Visit(models.Model):
    date = models.DateTimeField(default=datetime.now())
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)


class VisitComment(models.Model):
    visit_id = models.ForeignKey(Visit, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=800)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class PlaceMedia(models.Model):
    visit_id = models.ForeignKey(Visit, on_delete=models.CASCADE, blank=True, null=True)
    media_url = models.TextField(max_length=800)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)



