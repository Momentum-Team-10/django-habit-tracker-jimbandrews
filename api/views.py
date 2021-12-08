from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from tracker.models import Habit, DailyRecord
from .serializers import HabitSerializer, RecordSerializer


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


class RecordListView(RetrieveUpdateDestroyAPIView):
    queryset = DailyRecord.objects.all()
    serializer_class = RecordSerializer
    lookup_field = 'habit'
    lookup_url_kwarg = 'pk'

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = RecordSerializer(queryset, many=True)
        return Response(serializer.data)
