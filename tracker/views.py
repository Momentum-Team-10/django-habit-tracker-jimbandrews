from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Habit, DailyRecord
from .forms import DailyRecordForm, HabitForm, RecordDateForm
from datetime import date

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
def habit_details(request, pk):
    if request.method == "GET":
        form = RecordDateForm()
    else:
        form = RecordDateForm(data=request.POST)
        date_str = form['date'].value()
        date_obj = date.fromisoformat(date_str)
        year = date_obj.year
        month = date_obj.month
        day = date_obj.day
        return redirect('record_data', pk=pk, year=year, month=month, day=day)
    habit = get_object_or_404(Habit, pk=pk)
    records = DailyRecord.objects.filter(
        habit_id=habit
    ).exclude(
        quantity=None
    )
    return render(request, 'tracker/habit_details.html', {"habit": habit, "records": records, "form": form})


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
            return redirect('habit_details')
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


@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "GET":
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect('habit_details', pk=pk)
    return render(request, 'tracker/edit_habit.html', {"form": form, "habit": habit})


@login_required
def record_data(request, pk, year, month, day):
    habit = get_object_or_404(Habit, pk=pk)
    record_date = date(year, month, day)
    record, created = DailyRecord.objects.get_or_create(habit_id=habit, date=record_date)
    if request.method == "GET":
        form = DailyRecordForm(instance=record)
    else:
        form = DailyRecordForm(data=request.POST, instance=record)
        if form['quantity'].value() == '' and created:
            record.delete()
            return redirect('habit_details', pk=pk)
        elif form.is_valid():
            form.save()
            return redirect('habit_details', pk=pk)
    return render(request, 'tracker/record_data.html', {"form": form, "habit": habit, "record_date": record_date, "record": record, "created":created})


@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "POST":
        habit.delete()
        return redirect('user_profile')
    else:
        return render(request, "tracker/delete_habit.html", {"habit": habit})