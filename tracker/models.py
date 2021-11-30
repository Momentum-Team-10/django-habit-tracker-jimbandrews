from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

# Create your models here.
class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Habit(models.Model):
    name = models.CharField(max_length=75)
    target = models.IntegerField(validators=[MinValueValidator(0)])