from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
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


class RecordListView(RetrieveUpdateDestroyAPIView):
    queryset = DailyRecord.objects.all()
    serializer_class = RecordSerializer
    lookup_field = 'habit'
    lookup_url_kwarg = 'pk'

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = RecordSerializer(queryset, many=True)
        return Response(serializer.data)


# ViewSets
class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]


class RecordViewSet(ModelViewSet):
    queryset = DailyRecord.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [AllowAny]
