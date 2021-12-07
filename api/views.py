from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from tracker.models import Habit
from .serializers import HabitSerializer


class HabitListView(APIView):
    """
    List all habits
    """

    def get(self, request, format=None):
        """
        Create a response that includes a list of habits
        """
        habits = Habit.objects.all() #queryset
        serializer = HabitSerializer(habits, many=True)

        return Response(serializer.data)
