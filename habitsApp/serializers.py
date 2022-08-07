from rest_framework import serializers
from .models import HabitCategory, Habit, HabitMeasures


class HabitCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitCategory
        fields = ['user', 'name', 'description', 'icon']
