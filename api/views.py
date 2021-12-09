from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from datetime import date
from tracker.models import Habit, DailyRecord
from .serializers import HabitSerializer, RecordSerializer

# Generic Views
class HabitListView(ListCreateAPIView):
    """
    List all habits
    """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDetailView(RetrieveUpdateDestroyAPIView):
    '''
    See a single habit
    '''

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class RecordListView(ListCreateAPIView):
    serializer_class = RecordSerializer

    def get_queryset(self):
        queryset = DailyRecord.objects.filter(habit_id=self.kwargs["pk"])
        return queryset


class RecordDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = RecordSerializer

    def get_queryset(self):
        queryset = DailyRecord.objects.filter(habit_id=self.kwargs["pk"])
        return queryset

    def get_object(self):
        record_date = date(self.kwargs["year"], self.kwargs["month"], self.kwargs["day"])
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, date=record_date)
        self.check_object_permissions(self.request, obj)
        return obj


# ViewSets
class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]


class RecordViewSet(ModelViewSet):
    queryset = DailyRecord.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [AllowAny]
