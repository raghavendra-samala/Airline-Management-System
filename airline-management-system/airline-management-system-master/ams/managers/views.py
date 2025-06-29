from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from user_accounts.decorators import manager_required
from airlines.models import Airport, Flight, Trip, AirplaneType
from passengers.models import Tickets
from django import forms
from datetime import date, time, timedelta
from .forms import TripForm, IntervalForm, SearchForm, SearchForm1, TypeForm, SelectTypeForm


# Create your views here.
@login_required(login_url="/user_accounts/login/")
@manager_required
def manager_homepage(request):
    return render(request, 'managers/manager_homepage.html')


occupancy = []


@login_required(login_url="/user_accounts/login/")
@manager_required
def check_occupancy(request):
    if request.method == 'POST':
        form = SearchForm1(request.POST)

        if form.is_valid():
            occupancy.clear()
            occupancy.append(form.cleaned_data['from_airport'])
            occupancy.append(form.cleaned_data['to_airport'])
            occupancy.append((form.cleaned_data['day']))

        return redirect('managers:view_occupancy')
    else:
        form = SearchForm1()
        return render(request, 'managers/occupancy.html', {'form': form})


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + timedelta(days_ahead)


def view_occupancy(request):
    fli = []
    flights = Flight.objects.all().order_by('departure_time')
    for flight in flights:
        if flight.from_airport == occupancy[0] and flight.to_airport == occupancy[1]:
            week = timedelta(days=7)
            today = date.today()
            day1 = 0
            if occupancy[2] == 'monday':
                day1 = 0
            if occupancy[2] == 'tuesday':
                day1 = 1
            if occupancy[2] == 'wednesday':
                day1 = 2
            if occupancy[2] == 'thursday':
                day1 = 3
            if occupancy[2] == 'friday':
                day1 = 4
            if occupancy[2] == 'saturday':
                day1 = 5
            if occupancy[2] == 'sunday':
                day1 = 6

            day2 = next_weekday(today, day1) + week
            day3 = day2 + week
            day4 = day3 + week
            day5 = day2 - week
            day6 = day5 - week
            # if flight.journey_date > date.today():
            if flight.journey_date == day2 or flight.journey_date == day3 or flight.journey_date == day4 or flight.journey_date == day5 or flight.journey_date == day6:
                fli.append(flight)

            occupancy_rate = 0

            occupancy_rate = []

            for fl in fli:
                occu = fl.first_class_occupancy_number + fl.business_class_occupancy_number + fl.economy_class_occupancy_number
                tot = fl.first_class_seats + fl.business_class_seats + fl.economy_class_seats
                occupancy_rate.append((occu / tot))

    return render(request, 'managers/view_occupancy.html',
                  {'from': occupancy[0], 'to': occupancy[1], 'day': occupancy[2], 'flights': fli})


@login_required(login_url="/user_accounts/login/")
@manager_required
def change_schedule(request):
    return render(request, 'managers/schedule.html')


@login_required(login_url="/user_accounts/login/")
@manager_required
def get_profits(request):
    if request.method == 'POST':
        flights = Flight.objects.all().order_by('journey_date')
        flights_list = []
        total_revenue = 0

        form = IntervalForm(request.POST)

        if form.is_valid():
            lowerlimit = form.cleaned_data['from_date']
            upperlimit = form.cleaned_data['to_date']
            for fli in flights:
                if fli.journey_date <= lowerlimit:
                    continue
                elif fli.journey_date >= upperlimit:
                    continue
                else:
                    flights_list.append(fli)

            for fli in flights_list:
                total_revenue += fli.profits

            return render(request, 'managers/totalprofits.html',
                          {'total_revenue': total_revenue, 'lowerlimit': lowerlimit, 'upperlimit': upperlimit})
    else:
        form = IntervalForm()
        return render(request, 'managers/profits.html', {'form': form})


info = {}
trip_details = []


@login_required(login_url="/user_accounts/login/")
@manager_required
def change_costs(request):
    if request.method == 'POST':
        form = SelectTypeForm(request.POST)

        if form.is_valid():
            trip_details.clear()
            trip_details.append(form.cleaned_data['choice'])

        return redirect('managers:modify')
    else:
        form = SelectTypeForm()
    return render(request, 'managers/change_costs.html', {'form': form})


@login_required(login_url="/user_accounts/login/")
@manager_required
def modify_costs(request):
    if request.method == 'POST':
        # current = get_object_or_404(AirplaneType, airplane_type=trip_details[0].airplane_type)
        form = TypeForm(instance=trip_details[0], data=request.POST)

        if form.is_valid():
            current = form.save(commit=False)
            form.save()
        return redirect('managers:manager')
    else:
        form = TypeForm(instance=trip_details[0])
    return render(request, 'managers/modify_costs.html', {'form': form})


@login_required(login_url="/user_accounts/login/")
@manager_required
def delete_flight(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            trip_details.clear()
            trip_details.append(form.cleaned_data['from_airport'])
            trip_details.append(form.cleaned_data['to_airport'])
            trip_details.append((form.cleaned_data['day']))

        return redirect('managers:search')
    else:
        form = SearchForm()
        return render(request, 'managers/delete_flight.html', {'form': form})


@login_required(login_url="/user_accounts/login/")
@manager_required
def search_flights(request):
    fli = []
    flights = Flight.objects.all().order_by('flight_id')
    for flight in flights:
        if flight.from_airport == trip_details[0] and flight.to_airport == trip_details[1]:
            week = timedelta(days=7)
            today = date.today()
            day1 = 0
            if trip_details[2] == 'monday':
                day1 = 0
            if trip_details[2] == 'tuesday':
                day1 = 1
            if trip_details[2] == 'wednesday':
                day1 = 2
            if trip_details[2] == 'thursday':
                day1 = 3
            if trip_details[2] == 'friday':
                day1 = 4
            if trip_details[2] == 'saturday':
                day1 = 5
            if trip_details[2] == 'sunday':
                day1 = 6

            day2 = next_weekday(today, day1) + week
            day3 = day2 + week
            day4 = day3 + week
            if flight.journey_date > date.today():
                if flight.journey_date == day2 or flight.journey_date == day3 or flight.journey_date == day4:
                    fli.append(flight)
    return render(request, 'managers/search_flights.html', {'flights': fli})


def is_new_possible():
    fli = 0
    trips = Trip.objects.all()
    for trip in trips:
        if trip_details[3] == trip.type and trip.day == trip_details[2]:
            a = trip.arrival_time
            b = trip.departure_time
            c = trip_details[4]
            d = trip_details[5]
            # print(str(a) + "||" + str(b) + "||" + str(c) + "||" + str(d))
            if (b <= c <= a) or (b <= d <= a):
                fli += 1
    # print("Yay this many  " + str(fli) + "  Flights")
    if trip_details[3].count > fli:
        return True
    return False


@login_required(login_url="/user_accounts/login/")
@manager_required
def add_flight(request):
    if request.method == 'POST':
        form = TripForm(request.POST, request.FILES)
        if form.is_valid():
            trip_details.clear()
            trip_details.append(form.cleaned_data['from_airport'])
            trip_details.append(form.cleaned_data['to_airport'])
            trip_details.append((form.cleaned_data['day']))
            trip_details.append((form.cleaned_data['type']))
            trip_details.append((form.cleaned_data['arrival_time']))
            trip_details.append((form.cleaned_data['departure_time']))
            if is_new_possible():
                form.save()
                return redirect('managers:manager')
            else:
                return redirect('managers:add')

    else:
        form = TripForm()
    return render(request, 'managers/add_flight.html', {'form': form})


@login_required(login_url="/user_accounts/login/")
@manager_required
def del_flight(request, slug):
    current = Flight.objects.get(slug=slug)
    current.delete()
    return redirect('managers:manager')