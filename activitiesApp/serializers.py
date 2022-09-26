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


class ActivityListSerializer(serializers.ModelSerializer):
    category = ActivityCategorySerializer(many=False, read_only=True)
    class Meta:
        model = Activity
        fields = [
            'id',
            'name',
            'color',
            'category',
            'description'
        ]

    def create(self, validated_data):
        activity = Activity.objects.create(**validated_data)
        return activity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            'id',
            'name',
            'color',
            'category',
            'description',
            'user'
        ]
