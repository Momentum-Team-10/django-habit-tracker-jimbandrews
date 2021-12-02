from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Habit, DailyRecord

# Create your views here.

def guest_home(request):
    return render(request, 'tracker/guest.html')


@login_required
def user_profile(request):
    user = request.user
    habits = Habit.objects.filter(user_id=user.pk)
    return render(request, 'tracker/profile.html', {"user": user, "habits": habits})