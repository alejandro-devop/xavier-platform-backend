from rest_framework import serializers
from activitiesApp.serializers import ActivityCategorySerializer
from .models import Task


class TaskStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'title',
            'user',
            'category',
            'description',
            'date_line',
            'is_urgent',
            'priority'
        ]


class TaskListSerializer(serializers.ModelSerializer):
    category = ActivityCategorySerializer(many=False, read_only=True)
    class Meta:
        model = Task
        fields = [
            'title',
            'category',
            'description',
            'is_completed',
            'is_canceled',
            'date_line',
            'is_urgent',
            'priority',
        ]
