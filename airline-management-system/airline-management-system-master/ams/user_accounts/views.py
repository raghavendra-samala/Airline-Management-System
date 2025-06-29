from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import PassengerSignUpForm, ManagerSignUpForm
from .models import User
from django.contrib import messages
from django.views.generic import CreateView


def choose_view(request):
    return render(request, 'user_accounts/choose_type.html')


"""
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # log the user in
            return redirect('passengers:passenger')
    else:
        form = UserCreationForm()
    return render(request, 'user_accounts/signup.html', {'form': form})
"""


class PassengerSignup(CreateView):
    model = User
    form_class = PassengerSignUpForm
    template_name = 'user_accounts/passenger_signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('passengers:passenger')


class ManagerSignup(CreateView):
    model = User
    form_class = ManagerSignUpForm
    template_name = 'user_accounts/manager_signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('managers:manager')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Login the user
            user = form.get_user()
            if user is not None:
                login(request, user)
                if user.is_Passenger:
                    return redirect('passengers:passenger')
                if user.is_Manager:
                    return redirect('managers:manager')

    else:
        form = AuthenticationForm()
    return render(request, 'user_accounts/login.html', {'form': form})


def logout_confirm(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'user_accounts/logout_confirm.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')
