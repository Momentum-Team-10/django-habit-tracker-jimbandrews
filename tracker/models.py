from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from autoslug import AutoSlugField
from datetime import date, datetime

# Create your models here.
class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Habit(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'user'], name="unique_habit")
        ]

    name = models.CharField(max_length=75)
    target = models.IntegerField(validators=[MinValueValidator(0)])
    units = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='name', null=True)

    def __repr__(self):
        return f"<Habit name={self.name}>"

    def __str__(self):
        return self.name


class DailyRecord(models.Model):
    quantity = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    date = models.DateField(validators=[MaxValueValidator(date.today())])
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE, unique_for_date="date", related_name="records")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'habit'], name="unique_daily_record")
        ]
        ordering = ['date']

    def __repr__(self):
        return f"<DailyRecord habit={self.habit}>"

    def __str__(self):
        return self.habit