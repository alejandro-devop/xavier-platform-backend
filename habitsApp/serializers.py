from rest_framework import serializers
from .models import HabitCategory, Habit


class HabitCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitCategory
        fields = ['id', 'user', 'name', 'description', 'icon']


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = [
            'id',
            'user',
            'activity',
            'measure',
            'name',
            'description',
            'should_avoid',
            'should_keep',
            'is_counter',
            'is_timer',
            'days',
            'streak',
            'max_streak',
            'start_date',
            'end_date'
        ]
