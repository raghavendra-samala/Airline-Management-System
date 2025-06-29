from django.test import TestCase, Client
from django.urls import reverse
from passengers.models import Tickets
from airlines.models import *
from user_accounts.models import User
import datetime
from passengers.views import trip_details


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='john',
                                              email='jlennon@beatles.com',
                                              password='Gokul@001',
                                              is_Passenger=True,
                                              balance=500000)
        self.perlAir = Airline.objects.create(name='PerlAir')
        self.Mumbai = Airport.objects.create(name = 'Mumbai')
        self.Mumbai.save()
        self.Hyderabad = Airport.objects.create(name = 'Hyderaad')
        self.Hyderabad.save()
        self.Chennai = Airport.objects.create(name='Chennai')
        self.Chennai.save()
        self.Delhi = Airport.objects.create(name='Delhi')
        self.Delhi.save()
        self.first_class747 = FirstClass.objects.create(seat=2, load_factor=3.00)
        self.economy_class747 = EconomyClass.objects.create(seat=5, load_factor=1.25)
        self.business_class747 = BusinessClass.objects.create(seat=3, load_factor=2.00)
        self.boeing747 = AirplaneType.objects.create(
            first_class=self.first_class747,
            economy_class=self.economy_class747,
            business_class=self.business_class747,
            airplane_type='boeing747',
            cost_per_km=5.00,
            fare_per_km=10.00,
            basic_cost=1000.00,
            count=10
        )
        self.flight1 = Flight.objects.create(
            airline=self.perlAir,
            distance=700,
            type=self.boeing747,
            first_class_seats=self.boeing747.first_class.seat,
            business_class_seats=self.boeing747.business_class.seat,
            economy_class_seats=self.boeing747.economy_class.seat,
            from_airport=self.Mumbai,
            to_airport=self.Hyderabad,
            journey_date=date.today(),
            departure_time=datetime.time(hour=10, minute=0, second=0),
            arrival_time=datetime.time(hour=11, minute=45, second=0)
        )
        self.flight2 = Flight.objects.create(
            airline=self.perlAir,
            distance=500,
            type=self.boeing747,
            first_class_seats=self.boeing747.first_class.seat,
            business_class_seats=self.boeing747.business_class.seat,
            economy_class_seats=self.boeing747.economy_class.seat,
            from_airport=self.Hyderabad,
            to_airport=self.Chennai,
            journey_date=date.today(),
            departure_time=datetime.time(hour=10, minute=0, second=0),
            arrival_time=datetime.time(hour=11, minute=45, second=0)
        )
        self.ticket1 = Tickets.objects.create(
            booking_id=self.flight2.slug,
            from_station='Hyderabad',
            to_station='Chennai',
            seat_type='economy',
            seat_number=5,
            ticket_holder=self.user1,
            fare=self.flight2.economy_class_fare,
            journey_date = self.flight2.journey_date
        )
        self.ticket2 = Tickets.objects.create(
            booking_id=self.flight1.slug,
            from_station='Mumbai',
            to_station='Hyderabad',
            seat_type='first',
            seat_number=5,
            ticket_holder=self.user1,
            fare=self.flight1.first_class_fare,
            journey_date=self.flight1.journey_date
        )
        self.ticket3 = Tickets.objects.create(
            booking_id=self.flight1.slug,
            from_station='Mumbai',
            to_station='Hyderabad',
            seat_type='economy',
            seat_number=5,
            ticket_holder=self.user1,
            fare=self.flight1.economy_class_fare,
            journey_date=self.flight1.journey_date
        )
        self.ticket4 = Tickets.objects.create(
            booking_id=self.flight1.slug,
            from_station='Mumbai',
            to_station='Hyderabad',
            seat_type='business',
            seat_number=5,
            ticket_holder=self.user1,
            fare=self.flight1.business_class_fare,
            journey_date=self.flight1.journey_date
        )
        self.login = self.client.login(username='john', password='Gokul@001')
        self.homepage = reverse('passengers:passenger')
        self.ticket_detail = reverse('passengers:ticket', args=[self.ticket4.slug])
        self.book_ticket = reverse('passengers:book')
        self.search_flights = reverse('passengers:search')
        self.details_of_flight  = reverse('passengers:detail',args = [self.flight2.slug])
        self.flight_detail = reverse('passengers:flight',args = [self.flight1.slug])
        self.del_ticket = reverse('passengers:del_ticket',args = [self.ticket3.slug])
        self.modify_ticket = reverse('passengers:modify_ticket',args = [self.ticket2.slug])
        self.see_ticket = reverse('passengers:trips')

    def test_homepage(self):
        response = self.client.get('/passengers/')
        self.assertEquals(response.status_code,200 )
        self.assertTemplateUsed(response, 'passengers/passenger_homepage.html')

    def test_ticket_detail(self):
        response = self.client.get(self.ticket_detail)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'passengers/ticket_detail.html')

    def test_book_ticket_get(self):
        response1 = self.client.get(self.book_ticket)
        self.assertEquals(response1.status_code,200)
        self.assertTemplateUsed(response1, 'passengers/book_ticket.html')

        response2 = self.client.post(self.book_ticket,{
            'from_airport' : self.Hyderabad,
            'to_airport' : self.Chennai,
            'today1' : date.today(),
            'seat_type' : 'business class',
        })

        self.assertEquals(response2.status_code,302)
        self.assertRedirects(response2,'/passengers/search/')

    def test_details_of_flights(self):
        response = self.client.get(self.details_of_flight)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'passengers/details_of_flight.html')

    def test_add_details(self):
        response1 = self.client.get(reverse('passengers:details'))
        self.assertEquals(response1.status_code,200)
        self.assertTemplateUsed(response1,'passengers/add_details.html')


    def test_flight_detail(self):
        response = self.client.get(self.flight_detail)
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,'/passengers/add_details/')

    def test_del_ticket(self):
        response = self.client.get(self.del_ticket)
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,'/passengers/')
        
    def test_modify_ticket(self):
        response = self.client.get(self.modify_ticket)
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,'/passengers/book_ticket/')

    def test_see_tickets(self):
        response = self.client.get(self.see_ticket)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'passengers/upcoming_trips.html')

    def test_add_balance(self):
        response1 = self.client.get(reverse('passengers:balance'))
        self.assertEquals(response1.status_code,200)
        self.assertTemplateUsed(response1,'passengers/add_balance.html')

        response2 = self.client.post(reverse('passengers:balance'),{
            'balance' : 20000
        })
        self.assertEquals(response2.status_code,302)
        self.assertRedirects(response2,'/passengers/')

    def test_choose_seat(self):
        response1 = self.client.get(reverse('passengers:choose_seat',args=[self.flight1.slug]))
        self.assertEquals(response1.status_code,200)
        self.assertTemplateUsed(response1,'passengers/choose_seat.html')
















