from rest_framework import serializers
from .models import HabitMeasures


class MeasuresSerializer(serializers.ModelSerializer):

    class Meta:
        model = HabitMeasures
        fields = ['id', 'user', 'name', 'abbreviation']