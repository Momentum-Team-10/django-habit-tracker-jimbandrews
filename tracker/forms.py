from django import forms
from .models import Habit, DailyRecord


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'target', 'units',]


class DailyRecordForm(forms.ModelForm):
    class Meta:
        model = DailyRecord
        fields = ['quantity', 'date',]