from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from datetime import date
from tracker.models import Habit, DailyRecord, User
from .serializers import HabitSerializer, RecordSerializer, UserSerializer
from .permissions import IsHabitCreator, IsRecordCreator

# Generic Views
class HabitListView(ListCreateAPIView):
    """
    List all habits
    """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsHabitCreator]

    def get_queryset(self):
        queryset = Habit.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitDetailView(RetrieveUpdateDestroyAPIView):
    '''
    See a single habit
    '''

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsHabitCreator]

    def get_queryset(self):
        queryset = Habit.objects.filter(user=self.request.user)
        return queryset


class RecordListView(ListCreateAPIView):
    '''
    List all records for a habit
    '''
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated, IsRecordCreator]

    def get_queryset(self):
        queryset = DailyRecord.objects.filter(habit_id=self.kwargs["pk"])
        return queryset
    def perform_create(self, serializer):
        serializer.save(habit_id=self.kwargs["pk"])


class RecordDetailView(RetrieveAPIView):
    '''
    See a single record
    '''
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated, IsRecordCreator]

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


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
