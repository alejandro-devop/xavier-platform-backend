from rest_framework import serializers
from .models import ActivityCategory, Activity


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


class ActivitySerializer(serializers.ModelSerializer):
    category = ActivityCategorySerializer(many=True)
    class Meta:
        model = Activity
        fields = [
            'name',
            'color',
            'category',
            'description'
        ]