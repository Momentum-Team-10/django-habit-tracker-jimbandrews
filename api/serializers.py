from rest_framework import serializers
from tracker.models import Habit

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Habit
        fields = (
            'pk',
            'name',
            'target',
            'units',
            'created_at',
            'user',
        )
