from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from .models import Passenger, Manager, User


class PassengerSignUpForm(UserCreationForm):
    phone_number = forms.CharField(required=True)
    email_id = forms.CharField(required=True)
    location = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_Passenger = True
        user.email_id = self.cleaned_data.get('email_id')
        user.save()
        passenger = Passenger.objects.create(user=user)
        passenger.phone_number = self.cleaned_data.get('phone_number')
        passenger.location = self.cleaned_data.get('location')
        passenger.save()
        return user


class ManagerSignUpForm(UserCreationForm):
    email_id = forms.CharField(required=True)
    id = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_Manager = True
        user.email_id = self.cleaned_data.get('email_id')
        user.save()
        manager = Manager.objects.create(user=user)
        manager.id = self.cleaned_data.get('id')
        manager.save()
        return user
