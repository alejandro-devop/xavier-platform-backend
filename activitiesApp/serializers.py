from rest_framework import serializers
from .models import ActivityCategory


class ActivityCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCategory
        fields = [
            'id',
            'user',
            'name',
            'color',
            'description',
            'icon',
            'is_rest',
            'is_work',
            'is_learning',
            'is_self_care',
            'is_exercise'
        ]
