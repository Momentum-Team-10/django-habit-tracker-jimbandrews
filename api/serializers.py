from rest_framework import serializers
from tracker.models import Habit, DailyRecord


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyRecord
        fields = (
            'pk',
            'quantity',
            'date',
        )


class HabitSerializer(serializers.ModelSerializer):
    records = RecordSerializer(many=True, read_only=True)
    class Meta:
        model = Habit
        fields = (
            'pk',
            'name',
            'target',
            'units',
            'created_at',
            'user',
            'records'
        )
