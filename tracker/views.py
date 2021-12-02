from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Habit, DailyRecord
from .forms import HabitForm

# Create your views here.

def guest_home(request):
    if request.user.is_authenticated:
        return redirect("user_profile")
    else:
        return render(request, 'tracker/guest.html')


@login_required
def user_profile(request):
    user = request.user
    habits = Habit.objects.filter(user_id=user.pk)
    return render(request, 'tracker/profile.html', {"user": user, "habits": habits})


@login_required
def add_habit(request):
    if request.method == "GET":
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_id = request.user
            form.save()
            return redirect('user_profile')
    return render(request, 'tracker/add_habit.html', {'form': form})
