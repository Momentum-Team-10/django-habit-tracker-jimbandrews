from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from tracker.models import Habit
from .serializers import HabitSerializer


class HabitListView(ListAPIView):
    """
    List all habits
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
