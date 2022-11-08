from rest_framework import serializers
from activitiesApp.serializers import ActivityListSerializer
from .models import Routine, RoutineBlock


class RoutineStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = [
            'id',
            'user',
            'description',
            'initial_time',
            'interval',
            'is_monday',
            'is_tuesday',
            'is_wednesday',
            'is_thursday',
            'is_friday',
            'is_saturday',
            'is_sunday',
        ]


class RoutineBlockStoreSerializer(serializers.ModelSerializer):
    class Meta:
        models = RoutineBlock
        fields = [
            'routine',
            'activity',
            'time_from',
            'time_to',
            'should_notify',
            'notify_time'
        ]


class RoutineBlockListSerializer(serializers.ModelSerializer):
    activity = ActivityListSerializer

    class Meta:
        models = RoutineBlock
        fields = [
            'routine',
            'activity',
            'time_from',
            'time_to',
            'should_notify',
            'notify_time'
        ]


class RoutineSingleSerializer(serializers.ModelSerializer):
    # routine_block_set = ActivityListSerializer(many=True)

    class Meta:
        model = Routine
        fields = [
            'id',
            'user',
            'description',
            'initial_time',
            'interval',
            'is_monday',
            'is_tuesday',
            'is_wednesday',
            'is_thursday',
            'is_friday',
            'is_saturday',
            'is_sunday',
        ]
