from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from tracker.models import Habit
from .serializers import HabitSerializer


class HabitListView(ListCreateAPIView):
    """
    List all habits
    """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDetailView(RetrieveUpdateDestroyAPIView):
    '''
    providing a set for DRF to search within and display a single habit
    '''

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
