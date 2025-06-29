from django.test import TestCase, Client
from django.urls import reverse
from passengers.models import Tickets
from airlines.models import *
from user_accounts.models import User
import datetime
from managers.views import *


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.perlAir = Airline.objects.create(name='PerlAir')
        self.user1 = User.objects.create_user(username='pranav',
                                              email='jlennon@beatles.com',
                                              password='Gokul@001',
                                              is_Manager=True,
                                              balance=500000)
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
        self.Mumbai = Airport.objects.create(name="Mumbai")
        self.Hyderabad = Airport.objects.create(name="Hyderabad")
        self.Delhi = Airport.objects.create(name="Delhi")
        self.Chennai = Airport.objects.create(name="Chennai")
        self.flight1 = Flight.objects.create(
            airline=self.perlAir,
            distance=700,
            type=self.boeing747,
            first_class_seats=self.boeing747.first_class.seat,
            business_class_seats=self.boeing747.business_class.seat,
            economy_class_seats=self.boeing747.economy_class.seat,
            from_airport=self.Mumbai,
            to_airport=self.Hyderabad,
            journey_date=datetime.date(year=2021, month=4, day=7),
            departure_time=datetime.time(hour=10, minute=0, second=0),
            arrival_time=datetime.time(hour=11, minute=45, second=0)
        )
        self.flight2 = Flight.objects.create(
            airline=self.perlAir,
            distance=700,
            type=self.boeing747,
            first_class_seats=self.boeing747.first_class.seat,
            business_class_seats=self.boeing747.business_class.seat,
            economy_class_seats=self.boeing747.economy_class.seat,
            from_airport=self.Delhi,
            to_airport=self.Chennai,
            journey_date=datetime.date(year=2021, month=4, day=7),
            departure_time=datetime.time(hour=10, minute=0, second=0),
            arrival_time=datetime.time(hour=11, minute=45, second=0)
        )
        self.login = self.client.login(username='pranav', password='Gokul@001')
        self.check_occupancy = reverse('managers:check')

    def test_homepage(self):
        response = self.client.get('/managers/')
        self.assertEquals(response.status_code,200 )
        self.assertTemplateUsed(response, 'managers/manager_homepage.html')

    def test_check_occupancy(self):
        response1 = self.client.get(self.check_occupancy)
        self.assertEquals(response1.status_code,200)
        self.assertTemplateUsed(response1,'managers/occupancy.html')

        response2 = self.client.post(self.check_occupancy,{
            'from_airport' : self.Delhi,
            'to_airport' : self.Chennai,
            'day' : 'monday'
        })
        self.assertEquals(response2.status_code,302)
        self.assertRedirects(response2,'/managers/view_occupancy/')

    def test_view_occupancy(self):
        response = self.client.get(reverse('managers:view_occupancy'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'managers/view_occupancy.html')

    def test_change_schedule(self):
        response  = self.client.get(reverse('managers:change'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'managers/schedule.html')

    def test_get_profits(self):
        response1 = self.client.get(reverse('managers:profit'))
        self.assertEquals(response1.status_code,200)
        self.assertTemplateUsed(response1,'managers/profits.html')
        response2  = self.client.post(reverse('managers:profit'),{
            'from_date' :datetime.date(year=2021,month=2,day=3),
            'to_date' :datetime.date(year=2021,month=4,day=4)
        })
        if response2 is not None:
            self.assertEquals(response2.status_code, 200)
            self.assertTemplateUsed(response2, 'managers/totalprofits.html')

    def test_change_costs(self):
        response1 = self.client.get(reverse('managers:costs'))
        self.assertEquals(response1.status_code,200)
        self.assertTemplateUsed(response1,'managers/change_costs.html')

        response2 = self.client.post(reverse('managers:costs'),{
            'choice' : self.boeing747
        })
        self.assertEquals(response2.status_code,302)
        self.assertRedirects(response2,'/managers/modify_costs/')

    def test_modify_costs(self):
        response1 = self.client.get(reverse('managers:modify'))
        self.assertEquals(response1.status_code,200)
        self.assertTemplateUsed(response1,'managers/modify_costs.html')

        response2 = self.client.post(reverse('managers:modify'))
        self.assertEquals(response2.status_code, 302)
        self.assertRedirects(response2,'/managers/')

    def test_search_flight(self):
        response = self.client.get(reverse('managers:search'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'managers/search_flights.html')

    def test_delete_flight(self):
        response1 = self.client.get(reverse("managers:delete"))
        self.assertEquals(response1.status_code,200)
        self.assertTemplateUsed(response1,'managers/delete_flight.html')

        response2 = self.client.post(reverse('managers:delete'),{
            'from_airport' : self.Mumbai,
            'to_airport' : self.Delhi,
            'day' : 'monday'
        })
        self.assertEquals(response2.status_code,302)
        self.assertRedirects(response2,'/managers/search/')

    def test_del_flight(self):
        response = self.client.get(reverse("managers:del",args=[self.flight1.slug]))
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,'/managers/')

    def test_add_flights(self):
        response1 = self.client.get(reverse("managers:add"))
        self.assertEquals(response1.status_code,200)
        self.assertTemplateUsed(response1,'managers/add_flight.html')

        response2 = self.client.post(reverse("managers:add"),{
            'from_airport' : self.Mumbai,
            'to_airport' : self.Chennai,
            'day' : 'monday',
            'arrival_time' : datetime.time(hour=11, minute=45, second=0),
            'departure_time' : datetime.time(hour=10, minute=0, second=0)
        })
        self.assertEquals(response2.status_code,200)
















