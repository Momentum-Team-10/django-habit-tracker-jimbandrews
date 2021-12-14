from rest_framework import serializers
from tracker.models import Habit, DailyRecord, User


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


class UserSerializer(serializers.ModelSerializer):
    habits = HabitSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'first_name',
            'last_name',
            'email',
            'bio',
            'image_url',
            'is_staff',
            'is_active',
            'date_joined',
            'last_login',
            'habits'
        )