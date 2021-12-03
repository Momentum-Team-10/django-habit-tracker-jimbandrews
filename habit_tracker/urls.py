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
from tracker import views
import debug_toolbar

urlpatterns = [
    # admin pages
    path('admin/', admin.site.urls),
    # registration-redux pages
    path('accounts/', include('registration.backends.simple.urls')),
    # debug-toolbar pages
    path('__debug__/', include(debug_toolbar.urls)),
    # my app pages
    path('', views.guest_home, name="guest_home"),
    path('user/', views.user_profile, name="user_profile"),
    path('habit/add/', views.add_habit, name="add_habit"),
    path('habit/<int:pk>/add_record', views.add_record, name="add_record")
]
