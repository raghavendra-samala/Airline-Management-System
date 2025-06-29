from django.db import models
from django.contrib.auth.models import AbstractUser


# from ..passengers.models import Tickets


# Create your models here.
class User(AbstractUser):
    is_Passenger = models.BooleanField(default=False)
    is_Manager = models.BooleanField(default=False)
    email_id = models.EmailField(max_length=250, blank=True)
    balance = models.PositiveIntegerField(default=0)

    """email_id = models.EmailField
    def __str__(self):
        return self.email_id"""


class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    location = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.user.username


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    id = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
