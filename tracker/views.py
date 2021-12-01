from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Habit, DailyRecord

# Create your views here.

def guest_home(request):
    return render(request, 'tracker/guest.html')


@login_required
def user_profile(request, pk):
    return render(request, 'tracker/profile.html')