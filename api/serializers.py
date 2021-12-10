from rest_framework import serializers
from tracker.models import Habit, DailyRecord


class RecordSerializer(serializers.ModelSerializer):
    habit = serializers.StringRelatedField()
    class Meta:
        model = DailyRecord
        fields = (
            'pk',
            'habit',
            'quantity',
            'date',
        )


class RecordForHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyRecord
        fields = (
            'pk',
            'quantity',
            'date',
        )


class HabitSerializer(serializers.ModelSerializer):
    records = RecordForHabitSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()
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
