from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Habit, DailyRecord
from .forms import DailyRecordForm, HabitForm

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


@login_required
def add_record(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "GET":
        form = DailyRecordForm()
    else:
        form = DailyRecordForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.habit_id = habit
            form.save()
            return redirect('user_profile')
    return render(request, 'tracker/add_record.html', {"form": form, "habit": habit})
