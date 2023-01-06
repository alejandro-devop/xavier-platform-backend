from rest_framework import serializers
from .models import HabitCategory, Habit, HabitFollowUp
from activitiesApp.serializers import ActivityListSerializer
from settingsApp.serializers import MeasuresSerializer


class HabitCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitCategory
        fields = ['id', 'user', 'name', 'description', 'icon']


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = [
            'id',
            'category',
            'user',
            'activity',
            'measure',
            'category',
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
            'end_date',
            'timer_goal',
            'times_goal'
        ]


class HabitListSerializer(serializers.ModelSerializer):
    category = HabitCategorySerializer(many=False, read_only=True)
    activity = ActivityListSerializer(many=False, read_only=True)
    measure = MeasuresSerializer(many=False, read_only=True)

    class Meta:
        model = Habit
        fields = [
            'id',
            'user',
            'activity',
            'measure',
            'category',
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
            'end_date',
            'timer_goal',
            'times_goal',
            'daily_goal'
        ]


class HabitFollowUpSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = HabitFollowUp
        fields = [
            'user',
            'date',
            'started_date',
            'description',
            'habit',
            'time_spent',
            'daily_goal',
            'daily_target',
            'is_accomplished',
            'is_failed'
        ]


class HabitFollowUpListSerializer(serializers.ModelSerializer):
    habit = HabitListSerializer(many=False, read_only=True)

    class Meta:
        model = HabitFollowUp
        fields = [
            'id',
            'user',
            'date',
            'started_date',
            'description',
            'habit',
            'time_spent',
            'daily_goal',
            'daily_target',
            'is_accomplished',
            'is_failed'
        ]