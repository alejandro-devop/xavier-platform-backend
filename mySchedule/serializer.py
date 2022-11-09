from rest_framework import serializers
from activitiesApp.serializers import ActivityListSerializer
from .models import Routine, RoutineBlock


class RoutineStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = [
            'id',
            'title',
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
        depth = 1
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
    blocks = serializers.SerializerMethodField()

    class Meta:
        model = Routine
        fields = [
            'id',
            'title',
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
            'blocks'
        ]

    def get_blocks(self, routine):
        blocks = RoutineBlock.objects.filter(routine=routine.id)
        return RoutineBlockListSerializer(blocks, many=True).data

