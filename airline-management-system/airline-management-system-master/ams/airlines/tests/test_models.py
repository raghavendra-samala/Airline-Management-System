from django.test import TestCase
from airlines.models import Airline,Airport,EconomyClass,BusinessClass,FirstClass,AirplaneType,Flight,Schedule,Trip
import datetime
from django.template.defaultfilters import slugify

class TestModels(TestCase):

    def setUp(self):
        self.perlAir = Airline.objects.create(name='PerlAir')
        self.Hyderabad = Airport.objects.create(name='Hyderabad', slug=slugify('Hyderabad'))
        self.Hyderabad.save()
        self.Mumbai = Airport(name='Mumbai', slug=slugify('Mumbai'))
        self.Mumbai.save()
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
            airline = self.perlAir,
            distance = 700,
            type = self.boeing747,
            first_class_seats = self.boeing747.first_class.seat,
            business_class_seats= self.boeing747.business_class.seat,
            economy_class_seats= self.boeing747.economy_class.seat,
            from_airport = self.Mumbai,
            to_airport = self.Hyderabad,
            journey_date = datetime.date(year = 2021,month = 4,day = 7),
            departure_time=datetime.time(hour=10, minute=0, second=0),
            arrival_time=datetime.time(hour=11, minute=45, second=0)
        )
        self.mondaySchedule = Schedule.objects.create(day='Monday', airline=self.perlAir)
        self.HyderabadtoMumbaiOnMonday = Trip.objects.create(
            from_airport=self.Hyderabad,
            to_airport=self.Mumbai,
            type=self.boeing747,
            departure_time=datetime.time(hour=10, minute=0, second=0),
            arrival_time=datetime.time(hour=11, minute=45, second=0),
            day=self.mondaySchedule,
            distance=620
        )

    def test_airport_str(self):
        self.assertEquals(self.Hyderabad.name, str(self.Hyderabad))

    def test_airplane_type_str(self):
        self.assertEquals(self.boeing747.airplane_type, str(self.boeing747))

    def test_schedule_str(self):
        self.assertEquals(str(self.mondaySchedule),'Monday')

    def test_flight(self):
        self.assertEquals("mh2021-04-07",self.flight1.flight_id)
        self.assertEquals(str(self.flight1),self.flight1.flight_id)
        self.assertEquals(self.flight1.first_class_occupancy, '00')
        self.assertEquals(self.flight1.business_class_occupancy, '000')
        self.assertEquals(self.flight1.economy_class_occupancy, '00000')
        self.assertEquals(self.flight1.first_class_fare, 22000)
        self.assertEquals(self.flight1.business_class_fare, 15000)
        self.assertEquals(self.flight1.economy_class_fare, 9750)

    def test_trip(self):
        self.assertEquals(str(self.HyderabadtoMumbaiOnMonday),'MondayHM')



