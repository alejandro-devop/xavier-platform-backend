from rest_framework import serializers
from activitiesApp.serializers import ActivityCategorySerializer
from .models import Goal


class GoalStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = [
            'id',
            'category',
            'user',
            'name',
            'description',
            'dead_line_date'
        ]


class GoalListSerializer(serializers.ModelSerializer):
    category = ActivityCategorySerializer(many=False, read_only=True)

    class Meta:
        model = Goal
        fields = [
            'id',
            'category',
            'name',
            'description',
            'dead_line_date'
        ]