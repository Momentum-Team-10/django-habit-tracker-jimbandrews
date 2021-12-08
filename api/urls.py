from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HabitViewSet, RecordViewSet

'''
There are 2 versions of creating the api endpoints for this project.
To use one, comment out the other and edit line 3 so that you are importing the proper views.
'''

''' 1) urlpatterns if using ViewSets'''
router = DefaultRouter()
router.register(r'habits', HabitViewSet)
router.register(r'records', RecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


''' 2) urlpatterns if using Generic Views'''
# urlpatterns = [
#     path('api-auth/', include('rest_framework.urls')),
#     path('api/habits/', HabitListView.as_view(), name="api_habit_list"),
#     path('api/habits/<int:pk>/', HabitDetailView.as_view(), name="api_habit_detail"),
#     path('api/habits/<int:pk>/records/', RecordListView.as_view(), name = "api_record_list"),
# ]
