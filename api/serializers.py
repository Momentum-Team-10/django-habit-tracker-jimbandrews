from rest_framework import serializers
from tracker.models import Habit, DailyRecord


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyRecord
        fields = (
            'pk',
            'quantity',
            'date',
            'habit',
        )


class HabitSerializer(serializers.ModelSerializer):
        class Meta:
            model = Habit
            fields = (
                'pk',
                'name',
                'target',
                'units',
                'created_at',
                'user',
            )
