from django.shortcuts import render, redirect, HttpResponse
from .models import Tickets
from django import forms
from django.contrib.auth.decorators import login_required
from airlines.models import Airport, Flight
from user_accounts.decorators import passenger_required
from user_accounts.models import Passenger, User
from datetime import date, timedelta
from crispy_forms.helper import FormHelper

airport = Airport.objects.all().order_by('name')
pnr_global = 1



seat_type = [
    ('first class', 'First Class'),
    ('business class', 'Business Class'),
    ('economy class', 'Economy Class')
]

days = [
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ('saturday', 'Saturday')
]

Days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


# Create your views here.
@login_required(login_url="/user_accounts/login/")
@passenger_required
def passenger_homepage(request):
    return render(request, 'passengers/passenger_homepage.html')


@login_required(login_url="/user_accounts/login/")
@passenger_required
def ticket_detail(request, slug):
    ticket = Tickets.objects.get(slug=slug)
    return render(request, 'passengers/ticket_detail.html', {'ticket': ticket})


info = {}
trip_details = []
presentclasstype = ''


class DateInput(forms.DateInput):
    input_type = 'date'


class EditBalanceForm(forms.Form):
    card_number = forms.CharField(label='Card Number')
    expiry_date = forms.CharField(label='Expiry Date', widget=DateInput)
    cvv = forms.CharField(label='Enter CVV')
    balance = forms.IntegerField(label='Enter Money To ADD')


class PassengerDetailsForm(forms.Form):
    gender_list = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    name = forms.CharField(label='Name')
    age = forms.IntegerField(label='Age')
    gender = forms.CharField(label='Gender', widget=forms.Select(choices=gender_list))


@login_required(login_url="/user_accounts/login/")
@passenger_required
def add_details(request):
    if request.method == 'POST':
        form = PassengerDetailsForm(request.POST)
        ticket = None
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            ticket = Tickets.objects.get(slug=trip_details[0].slug)
            ticket.passenger_name = name
            ticket.passenger_age = age
            ticket.passenger_gender = gender
            ticket.save()

        return render(request, 'passengers/flight_detail.html', {'ticket': ticket, 'flight': trip_details[1]})
    else:
        form = PassengerDetailsForm()
        return render(request, 'passengers/add_details.html', {'form': form})


@login_required(login_url="/user_accounts/login/")
@passenger_required
def add_balance(request):
    if request.method == 'POST':
        form = EditBalanceForm(request.POST)

        if form.is_valid():
            balance = form.cleaned_data['balance']
            user = User.objects.get(username=request.user.username)
            user.balance += balance
            user.save()

        return redirect('passengers:passenger')
    else:
        form = EditBalanceForm()
        return render(request, 'passengers/add_balance.html', {'form': form})


class SearchForm(forms.Form):
    # from_airport = forms.CharField(label='From Airport', widget=forms.Select(choices=airport_list))
    # to_airport = forms.CharField(label='To Airport', widget=forms.Select(choices=airport_list))

    from_airport = forms.ModelChoiceField(label="From Airport", queryset=Airport.objects.all(), to_field_name="name")
    to_airport = forms.ModelChoiceField(label="To Airport", queryset=Airport.objects.all(), to_field_name="name")
    day1 = timedelta(days=1)
    today = date.today()
    todays = []
    for i in range(7):
        todays.append((today, today))
        today += day1
    today1 = forms.CharField(label='Date of Travel', widget=forms.Select(choices=todays))
    seat_type = forms.CharField(label="Seat Type", widget=forms.Select(choices=seat_type))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.use_custom_control = True


@login_required(login_url="/user_accounts/login/")
@passenger_required
def book_ticket(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            trip_details.clear()
            trip_details.append(form.cleaned_data['from_airport'])
            trip_details.append(form.cleaned_data['to_airport'])
            trip_details.append((form.cleaned_data['today1']))
            trip_details.append((form.cleaned_data['seat_type']))
            presentclasstype = trip_details[3]

        return redirect('passengers:search')
    else:
        form = SearchForm()
        return render(request, 'passengers/book_ticket.html', {'form': form})


@login_required(login_url="/user_accounts/login/")
@passenger_required
def search_flights(request):
    flights = Flight.objects.all().order_by('departure_time')
    fli = []
    for flight in flights:
        if flight.from_airport == trip_details[0] and flight.to_airport == trip_details[1]:
            if str(flight.journey_date) == str(trip_details[2]):
                fli.append(flight)
    return render(request, 'passengers/search_flights.html', {'flights': fli, 'class_searched': trip_details[3]})


@login_required(login_url="/user_accounts/login/")
@passenger_required
def see_tickets(request):
    tickets = Tickets.objects.all().order_by('booking_date')
    user_tickets = []
    for tick in tickets:
        if tick.ticket_holder == request.user:
            if not tick.journey_date < date.today():
                user_tickets.append(tick)
    return render(request, 'passengers/upcoming_trips.html', {'tickets': user_tickets})


@login_required(login_url="/user_accounts/login/")
@passenger_required
def flight_detail(request, slug):
    current = Flight.objects.get(slug=slug)

    fareamount = 0
    if trip_details[3] == 'first class':
        fareamount = current.first_class_fare
    elif trip_details[3] == 'business class':
        fareamount = current.business_class_fare
    elif trip_details[3] == 'economy class':
        fareamount = current.economy_class_fare
    else:
        fareamount = 15000

    no_of_tickets = Tickets.objects.count() + 1
    new_ticket = Tickets(booking_id=current.flight_id, from_station=current.from_airport, to_station=current.to_airport,
                         pnr=str(no_of_tickets),
                         slug=str(no_of_tickets), description="Happy Journey", ticket_holder=request.user,
                         seat_number=0,
                         journey_date=current.journey_date,
                         fare=fareamount)

    j = 0
    if trip_details[3] == "economy class":
        new_ticket.seat_type = "economy"
        for i in range(len(current.economy_class_occupancy)):
            j = i
            if current.economy_class_occupancy[i] == '0':
                print(i + 1)
                new_ticket.seat_number = i + 1
                current.economy_class_occupancy = current.economy_class_occupancy[
                                                  :i] + "1" + current.economy_class_occupancy[i + 1:]
                current.economy_class_occupancy_number += 1
                break

    if j == len(current.economy_class_occupancy):
        current.extra_requests += 1
        return render(request, 'passengers/no_seat.html')

    j = 0
    if trip_details[3] == "business class":
        new_ticket.seat_type = "business"
        for i in range(len(current.economy_class_occupancy)):
            j = i
            if current.business_class_occupancy[i] == '0':
                current.business_class_occupancy = current.business_class_occupancy[
                                                   :i] + "1" + current.business_class_occupancy[i + 1:]
                current.business_class_occupancy_number += 1
                print(i + 1)
                new_ticket.seat_number = i + 1
                break

    if j == len(current.economy_class_occupancy):
        current.extra_requests += 1
        return render(request, 'passengers/no_seat.html')

    j = 0
    if trip_details[3] == "first class":
        new_ticket.seat_type = "first"
        for i in range(len(current.economy_class_occupancy)):
            j = i
            if current.first_class_occupancy[i] == '0':
                print(i + 1)
                new_ticket.seat_number = i + 1
                print("before " + current.first_class_occupancy)
                current.first_class_occupancy = current.first_class_occupancy[:i] + "1" + current.first_class_occupancy[
                                                                                          i + 1:]
                current.first_class_occupancy_number += 1
                print("After " + current.first_class_occupancy)
                break

    if j == len(current.economy_class_occupancy):
        current.extra_requests += 1
        return render(request, 'passengers/no_seat.html')

    print(new_ticket.seat_number)

    if request.user.balance < new_ticket.fare:
        return redirect('passengers:balance')

    new_ticket.save()
    current.profits += new_ticket.fare
    current.save()
    trip_details.clear()
    trip_details.append(new_ticket)
    trip_details.append(current)
    return redirect('passengers:details')
    # return render(request, 'passengers/flight_detail.html', {'ticket': new_ticket, 'flight': current})


def del_ticket(request, slug):
    tik = Tickets.objects.get(slug=slug)
    username = str(tik.ticket_holder)
    user = User.objects.get(username=username)
    user.balance += tik.fare
    user.balance -= tik.fare/5
    current = Flight.objects.get(flight_id=tik.booking_id)
    if tik.seat_type == 'economy':
        index = tik.seat_number - 1
        current.economy_class_occupancy = current.economy_class_occupancy[
                                          :index] + "0" + current.economy_class_occupancy[index + 1:]
        current.economy_class_occupancy_number -= 1
    if tik.seat_type == 'business':
        index = tik.seat_number - 1
        current.business_class_occupancy = current.business_class_occupancy[
                                           :index] + "0" + current.business_class_occupancy[index + 1:]
        current.business_class_occupancy_number -= 1
    if tik.seat_type == 'first':
        index = tik.seat_number - 1
        current.first_class_occupancy = current.first_class_occupancy[:index] + "0" + current.first_class_occupancy[
                                                                                      index + 1:]
        current.first_class_occupancy_number -= 1

    user.save()
    current.profits -= tik.fare
    current.profits += tik.fare/5
    current.save()
    tik.delete()
    return redirect('passengers:passenger')


def modify_ticket(request, slug):
    tik = Tickets.objects.get(slug=slug)
    username = str(tik.ticket_holder)
    user = User.objects.get(username=username)
    user.balance += tik.fare
    user.balance -= tik.fare/5
    current = Flight.objects.get(flight_id=tik.booking_id)
    if tik.seat_type == 'economy':
        index = tik.seat_number - 1
        current.economy_class_occupancy = current.economy_class_occupancy[
                                          :index] + "0" + current.economy_class_occupancy[index + 1:]
        current.economy_class_occupancy_number -= 1
    if tik.seat_type == 'business':
        index = tik.seat_number - 1
        current.business_class_occupancy = current.business_class_occupancy[
                                           :index] + "0" + current.business_class_occupancy[index + 1:]
        current.business_class_occupancy_number -= 1
    if tik.seat_type == 'first':
        index = tik.seat_number - 1
        current.first_class_occupancy = current.first_class_occupancy[:index] + "0" + current.first_class_occupancy[
                                                                                      index + 1:]
        current.first_class_occupancy_number -= 1

    user.save()
    current.profits -= tik.fare
    current.profits += tik.fare / 5
    current.save()
    tik.delete()
    return redirect('passengers:book')


@login_required(login_url="/user_accounts/login/")
@passenger_required
def details_of_flight(request, slug):
    current = Flight.objects.get(slug=slug)
    economy = 0
    business = 0
    first = 0
    for i in range(len(current.economy_class_occupancy)):
        if current.economy_class_occupancy[i] == '0':
            economy += 1
    for i in range(len(current.business_class_occupancy)):
        if current.business_class_occupancy[i] == '0':
            business += 1
    for i in range(len(current.first_class_occupancy)):
        if current.first_class_occupancy[i] == '0':
            first += 1
    return render(request, 'passengers/details_of_flight.html',
                  {'flight': current, 'economy': economy, 'business': business, 'first': first,
                   'efare': current.economy_class_fare, 'bfare': current.business_class_fare,
                   'ffare': current.first_class_fare})


@login_required(login_url="/user_accounts/login/")
@passenger_required
def choose_seat(request, slug):
    current = Flight.objects.get(slug=slug)
    vacant = []
    seat = ""
    if trip_details[3] == "economy class":
        seat = "economy"
        for i in range(len(current.economy_class_occupancy)):
            if current.economy_class_occupancy[i] == '0':
                vacant.append((i, i))

    if trip_details[3] == "business class":
        seat = "business"
        for i in range(len(current.business_class_occupancy)):
            if current.business_class_occupancy[i] == '0':
                vacant.append((i + 1, i + 1))

    if trip_details[3] == "first class":
        seat = "first"
        for i in range(len(current.first_class_occupancy)):
            if current.first_class_occupancy[i] == '0':
                vacant.append((i + 1, i + 1))

    if len(vacant) == 0:
        render(request, 'passengers/no_seat.html')

    class ChooseForm(forms.Form):
        seat_number = forms.IntegerField(label="Choose the Seat Number", widget=forms.Select(choices=vacant))

    if request.method == 'POST':
        form = ChooseForm(request.POST)

        if form.is_valid():

            index = form.cleaned_data['seat_number'] - 1

            if trip_details[3] == "economy class":
                current.economy_class_occupancy = current.economy_class_occupancy[
                                                  :index] + "1" + current.economy_class_occupancy[index + 1:]
                current.economy_class_occupancy_number += 1

            if trip_details[3] == "first class":
                current.first_class_occupancy = current.first_class_occupancy[
                                                :index] + "1" + current.first_class_occupancy[index + 1:]
                current.first_class_occupancy_number += 1

            if trip_details[3] == "business class":
                current.business_class_occupancy = current.first_class_occupancy[
                                                   :index] + "1" + current.first_class_occupancy[index + 1:]
                current.business_class_occupancy_number += 1

            new_ticket = None

            if trip_details[3] == 'first class':
                fareamount = current.first_class_fare
            elif trip_details[3] == 'business class':
                fareamount = current.business_class_fare
            elif trip_details[3] == 'economy class':
                fareamount = current.economy_class_fare
            else:
                fareamount = 15000
            # fareamount = None if presentclasstype == 'first class': fareamount = current.type.basic_cost + ( (
            # current.type.fare_per_km )*(current.distance)*( current.type.first_class.load_factor ) ) elif
            # presentclasstype == 'business class': fareamount = current.type.basic_cost + ( (
            # current.type.fare_per_km )*(current.distance)*( current.type.business_class.load_factor ) ) elif
            # presentclasstype == 'economy class': fareamount = current.type.basic_cost + ( (
            # current.type.fare_per_km )*(current.distance)*( current.type.economy_class.load_factor ) )

            no_of_tickets = Tickets.objects.count() + 1

            new_ticket = Tickets(booking_id=current.flight_id, from_station=current.from_airport,
                                 to_station=current.to_airport, seat_type=seat, pnr=str(no_of_tickets),
                                 slug=str(no_of_tickets), description="Happy Journey", ticket_holder=request.user,
                                 seat_number=form.cleaned_data['seat_number'], journey_date=current.journey_date,
                                 fare=fareamount + 200)
            if request.user.balance < new_ticket.fare:
                return redirect('passengers:balance')

            new_ticket.save()
            current.profits += new_ticket.fare
            current.save()
            trip_details.clear()
            trip_details.append(new_ticket)
            trip_details.append(current)

        return redirect('passengers:details')

        # return render(request, 'passengers/flight_detail.html', {'ticket': new_ticket, 'flight': current})
    else:
        form = ChooseForm()
        return render(request, 'passengers/choose_seat.html', {'form': form, 'flight': current})
