"""habit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tracker import views as tracker_views
from api import views as api_views
import debug_toolbar

urlpatterns = [
    # admin pages
    path('admin/', admin.site.urls),
    # registration-redux pages
    path('accounts/', include('registration.backends.simple.urls')),
    # debug-toolbar pages
    path('__debug__/', include(debug_toolbar.urls)),
    # tracker pages
    path('', tracker_views.guest_home, name="guest_home"),
    path('user/', tracker_views.user_profile, name="user_profile"),
    path('habit/add/', tracker_views.add_habit, name="add_habit"),
    path('habit/<int:pk>/', tracker_views.habit_details, name="habit_details"),
    path('habit/<int:pk>/edit/', tracker_views.edit_habit, name="edit_habit"),
    path('habit/<int:pk>/<int:year>/<int:month>/<int:day>/', tracker_views.record_data, name="record_data"),
    path('habit/<int:pk>/delete', tracker_views.delete_habit, name="delete_habit"),
    # api endpoints with Generic Views
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/habits/', api_views.HabitListView.as_view(), name="api_habit_list"),
    # path('api/habits/<int:pk>/', api_views.HabitDetailView.as_view(), name="api_habit_detail"),
    # path('api/habits/<int:pk>/records/', api_views.RecordListView.as_view(), name = "api_record_list"),
    # api endpoints with ViewSets
    path('api/', include('api.urls')),
]
