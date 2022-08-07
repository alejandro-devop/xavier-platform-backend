from django.db import models
from django.contrib.auth.models import User


class UserMeta(models.Model):
    """Model for the user metadata"""
    account_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
