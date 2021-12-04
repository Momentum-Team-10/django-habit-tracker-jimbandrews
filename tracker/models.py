from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from autoslug import AutoSlugField

# Create your models here.
class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Habit(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'user_id'], name="unique_habit")
        ]

    name = models.CharField(max_length=75)
    target = models.IntegerField(validators=[MinValueValidator(0)])
    units = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='name', null=True)

    def __repr__(self):
        return f"<Habit name={self.name}>"

    def __str__(self):
        return self.name


class DailyRecord(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'habit_id'], name="unique_daily_record")
        ]

    quantity = models.IntegerField(null=True)
    date = models.DateField()
    habit_id = models.ForeignKey('Habit', on_delete=models.CASCADE, unique_for_date="date")
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"<DailyRecord habit={self.habit_id}"

    def __str__(self):
        return self.habit_id