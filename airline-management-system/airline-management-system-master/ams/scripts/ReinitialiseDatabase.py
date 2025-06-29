from airlines.models import Flight, Airport, AirplaneType, Airline, Schedule, Trip, FirstClass, EconomyClass, \
    BusinessClass
from django.utils.text import slugify
import datetime


def run(*args):
    # create Airline
    perlAir = Airline(name='PerlAir')
    perlAir.save()

    # create Airports
    Hyderabad = Airport(name='Hyderabad', slug=slugify('Hyderabad'))
    Mumbai = Airport(name='Mumbai', slug=slugify('Mumbai'))
    Delhi = Airport(name='Delhi', slug=slugify('Delhi'))
    Chennai = Airport(name='Chennai', slug=slugify('Chennai'))
    Bangalore = Airport(name='Bangalore', slug=slugify('Bangalore'))
    Kolkata = Airport(name='Kolkata', slug=slugify('Kolkata'))

    Hyderabad.save()
    Mumbai.save()
    Delhi.save()
    Chennai.save()
    Bangalore.save()
    Kolkata.save()

    # create Airplane Types

    first_class747 = FirstClass(seat=50, load_factor=3.00)
    first_class747.save()
    economy_class747 = EconomyClass(seat=300, load_factor=1.25)
    economy_class747.save()
    business_class747 = BusinessClass(seat=100, load_factor=2.00)
    business_class747.save()

    boeing747 = AirplaneType(
        first_class=first_class747,
        economy_class=economy_class747,
        business_class=business_class747,
        airplane_type='boeing747',
        cost_per_km=5.00,
        fare_per_km=10.00,
        basic_cost=1000.00,
        count=10
    )
    boeing747.save()

    #    airbus320 = AirplaneType(
    #        airplane_type = 'airbus320',
    #        first_class = FirstClass(seat = 10, load_factor = 3.00),
    #        economy_class = EconomyClass(seat = 100, load_factor = 1.25),
    #        business_class = BusinessClass(seat = 30, load_factor = 2.00),
    #        cost_per_km = 3.00,
    #        fare_per_km = 7.00,
    #        basic_cost = 700.00
    #    )
    #    airbus320.save()

    first_class787 = FirstClass(seat=25, load_factor=3.00)
    first_class787.save()
    economy_class787 = EconomyClass(seat=150, load_factor=1.25)
    economy_class787.save()
    business_class787 = BusinessClass(seat=50, load_factor=2.00)
    business_class787.save()

    boeing787 = AirplaneType(
        first_class=first_class787,
        economy_class=economy_class787,
        business_class=business_class787,
        airplane_type='boeing787',
        cost_per_km=5.00,
        fare_per_km=12.00,
        basic_cost=1200.00,
        count=10
    )
    boeing787.save()

    #    airbus350 = AirplaneType(
    #        airplane_type = 'airbus350',
    #        first_class = FirstClass(seat = 20, load_factor = 3.00),
    #        economy_class = EconomyClass(seat = 150, load_factor = 1.25),
    #        business_class = BusinessClass(seat = 75, load_factor = 2.00),
    #        cost_per_km = 4.00,
    #        fare_per_km = 8.00,
    #        basic_cost = 800.00
    #    )
    #    airbus350.save()

    first_class737 = FirstClass(seat=10, load_factor=3.00)
    first_class737.save()
    economy_class737 = EconomyClass(seat=120, load_factor=1.25)
    economy_class737.save()
    business_class737 = BusinessClass(seat=25, load_factor=2.00)
    business_class737.save()

    boeing737 = AirplaneType(
        airplane_type='boeing737',
        first_class=first_class737,
        economy_class=economy_class737,
        business_class=business_class737,
        cost_per_km=3.00,
        fare_per_km=8.00,
        basic_cost=700.00,
        count=10
    )
    boeing737.save()

    # creating Schedules
    mondaySchedule = Schedule(day='Monday', airline=perlAir)
    mondaySchedule.save()
    tuesdaySchedule = Schedule(day='Tuesday', airline=perlAir)
    tuesdaySchedule.save()
    wednesdaySchedule = Schedule(day='Wednesday', airline=perlAir)
    wednesdaySchedule.save()
    thursdaySchedule = Schedule(day='Thursday', airline=perlAir)
    thursdaySchedule.save()
    fridaySchedule = Schedule(day='Friday', airline=perlAir)
    fridaySchedule.save()
    saturdaySchedule = Schedule(day='Saturday', airline=perlAir)
    saturdaySchedule.save()
    sundaySchedule = Schedule(day='Sunday', airline=perlAir)
    sundaySchedule.save()

    #   create Trips for schedules

    #   Trips on Monday -----------------------------------------------------
    HyderabadtoMumbaiOnMonday = Trip(
        from_airport=Hyderabad,
        to_airport=Mumbai,
        type=boeing747,
        departure_time=datetime.time(hour=10, minute=0, second=0),
        arrival_time=datetime.time(hour=11, minute=45, second=0),
        day=mondaySchedule,
        distance=620
    )
    HyderabadtoMumbaiOnMonday.save()

    MumbaitoHyderabadOnMonday = Trip(
        from_airport=Mumbai,
        to_airport=Hyderabad,
        type=boeing747,
        departure_time=datetime.time(hour=13, minute=0, second=0),
        arrival_time=datetime.time(hour=14, minute=45, second=0),
        day=mondaySchedule,
        distance=620
    )
    MumbaitoHyderabadOnMonday.save()

    DelhitoMumbaiOnMonday = Trip(
        from_airport=Delhi,
        to_airport=Mumbai,
        type=boeing747,
        departure_time=datetime.time(hour=14, minute=0, second=0),
        arrival_time=datetime.time(hour=16, minute=30, second=0),
        day=mondaySchedule,
        distance=1200
    )
    DelhitoMumbaiOnMonday.save()

    MumbaitoDelhiOnMonday = Trip(
        from_airport=Mumbai,
        to_airport=Delhi,
        type=boeing747,
        departure_time=datetime.time(hour=17, minute=0, second=0),
        arrival_time=datetime.time(hour=19, minute=30, second=0),
        day=mondaySchedule,
        distance=1200
    )
    MumbaitoDelhiOnMonday.save()

    HyderabadtoDelhiOnMonday = Trip(
        from_airport=Hyderabad,
        to_airport=Delhi,
        type=boeing747,
        departure_time=datetime.time(hour=12, minute=0, second=0),
        arrival_time=datetime.time(hour=14, minute=30, second=0),
        day=mondaySchedule,
        distance=1300
    )
    HyderabadtoDelhiOnMonday.save()

    DelhitoHyderabadOnMonday = Trip(
        from_airport=Delhi,
        to_airport=Hyderabad,
        type=boeing747,
        departure_time=datetime.time(hour=16, minute=0, second=0),
        arrival_time=datetime.time(hour=18, minute=30, second=0),
        day=mondaySchedule,
        distance=1300
    )
    DelhitoHyderabadOnMonday.save()

    HyderabadtoBangaloreOnMonday = Trip(
        from_airport=Hyderabad,
        to_airport=Bangalore,
        type=boeing787,
        departure_time=datetime.time(hour=10, minute=0, second=0),
        arrival_time=datetime.time(hour=11, minute=15, second=0),
        day=mondaySchedule,
        distance=450
    )
    HyderabadtoBangaloreOnMonday.save()

    BangaloretoHyderabadOnMonday = Trip(
        from_airport=Bangalore,
        to_airport=Hyderabad,
        type=boeing787,
        departure_time=datetime.time(hour=12, minute=30, second=0),
        arrival_time=datetime.time(hour=13, minute=45, second=0),
        day=mondaySchedule,
        distance=450
    )
    BangaloretoHyderabadOnMonday.save()

    HyderabadtoKolkataOnMonday = Trip(
        from_airport=Hyderabad,
        to_airport=Kolkata,
        type=boeing737,
        departure_time=datetime.time(hour=17, minute=0, second=0),
        arrival_time=datetime.time(hour=19, minute=30, second=0),
        day=mondaySchedule,
        distance=1200
    )
    HyderabadtoKolkataOnMonday.save()

    KolkatatoHyderabadOnMonday = Trip(
        from_airport=Kolkata,
        to_airport=Hyderabad,
        type=boeing737,
        departure_time=datetime.time(hour=21, minute=0, second=0),
        arrival_time=datetime.time(hour=23, minute=30, second=0),
        day=mondaySchedule,
        distance=1200
    )
    KolkatatoHyderabadOnMonday.save()

    HyderabadtoChennaiOnMonday = Trip(
        from_airport=Hyderabad,
        to_airport=Chennai,
        type=boeing737,
        departure_time=datetime.time(hour=8, minute=0, second=0),
        arrival_time=datetime.time(hour=9, minute=30, second=0),
        day=mondaySchedule,
        distance=500
    )
    HyderabadtoChennaiOnMonday.save()

    ChennaitoHyderabadOnMonday = Trip(
        from_airport=Chennai,
        to_airport=Hyderabad,
        type=boeing737,
        departure_time=datetime.time(hour=11, minute=0, second=0),
        arrival_time=datetime.time(hour=12, minute=30, second=0),
        day=mondaySchedule,
        distance=500
    )
    ChennaitoHyderabadOnMonday.save()

    #   Trips on Tuesday ----------------------------------------------------

    HyderabadtoMumbaiOnTuesday = Trip(
        from_airport=Hyderabad,
        to_airport=Mumbai,
        type=boeing747,
        departure_time=datetime.time(hour=10, minute=0, second=0),
        arrival_time=datetime.time(hour=11, minute=45, second=0),
        day=tuesdaySchedule,
        distance=620
    )
    HyderabadtoMumbaiOnTuesday.save()

    MumbaitoHyderabadOnTuesday = Trip(
        from_airport=Mumbai,
        to_airport=Hyderabad,
        type=boeing747,
        departure_time=datetime.time(hour=13, minute=0, second=0),
        arrival_time=datetime.time(hour=14, minute=45, second=0),
        day=tuesdaySchedule,
        distance=620
    )
    MumbaitoHyderabadOnTuesday.save()

    DelhitoMumbaiOnTuesday = Trip(
        from_airport=Delhi,
        to_airport=Mumbai,
        type=boeing747,
        departure_time=datetime.time(hour=14, minute=0, second=0),
        arrival_time=datetime.time(hour=16, minute=30, second=0),
        day=tuesdaySchedule,
        distance=1200
    )
    DelhitoMumbaiOnTuesday.save()

    MumbaitoDelhiOnTuesday = Trip(
        from_airport=Mumbai,
        to_airport=Delhi,
        type=boeing747,
        departure_time=datetime.time(hour=17, minute=0, second=0),
        arrival_time=datetime.time(hour=19, minute=30, second=0),
        day=tuesdaySchedule,
        distance=1200
    )
    MumbaitoDelhiOnTuesday.save()

    HyderabadtoDelhiOnTuesday = Trip(
        from_airport=Hyderabad,
        to_airport=Delhi,
        type=boeing747,
        departure_time=datetime.time(hour=12, minute=0, second=0),
        arrival_time=datetime.time(hour=14, minute=30, second=0),
        day=tuesdaySchedule,
        distance=1300
    )
    HyderabadtoDelhiOnTuesday.save()

    DelhitoHyderabadOnTuesday = Trip(
        from_airport=Delhi,
        to_airport=Hyderabad,
        type=boeing747,
        departure_time=datetime.time(hour=16, minute=0, second=0),
        arrival_time=datetime.time(hour=18, minute=30, second=0),
        day=tuesdaySchedule,
        distance=1300
    )
    DelhitoHyderabadOnTuesday.save()

    HyderabadtoBangaloreOnTuesday = Trip(
        from_airport=Hyderabad,
        to_airport=Bangalore,
        type=boeing787,
        departure_time=datetime.time(hour=10, minute=0, second=0),
        arrival_time=datetime.time(hour=11, minute=15, second=0),
        day=tuesdaySchedule,
        distance=450
    )
    HyderabadtoBangaloreOnTuesday.save()

    BangaloretoHyderabadOnTuesday = Trip(
        from_airport=Bangalore,
        to_airport=Hyderabad,
        type=boeing787,
        departure_time=datetime.time(hour=12, minute=30, second=0),
        arrival_time=datetime.time(hour=13, minute=45, second=0),
        day=tuesdaySchedule,
        distance=450
    )
    BangaloretoHyderabadOnTuesday.save()

    HyderabadtoKolkataOnTuesday = Trip(
        from_airport=Hyderabad,
        to_airport=Kolkata,
        type=boeing737,
        departure_time=datetime.time(hour=17, minute=0, second=0),
        arrival_time=datetime.time(hour=19, minute=30, second=0),
        day=tuesdaySchedule,
        distance=1200
    )
    HyderabadtoKolkataOnTuesday.save()

    KolkatatoHyderabadOnTuesday = Trip(
        from_airport=Kolkata,
        to_airport=Hyderabad,
        type=boeing737,
        departure_time=datetime.time(hour=21, minute=0, second=0),
        arrival_time=datetime.time(hour=23, minute=30, second=0),
        day=tuesdaySchedule,
        distance=1200
    )
    KolkatatoHyderabadOnTuesday.save()

    HyderabadtoChennaiOnTuesday = Trip(
        from_airport=Hyderabad,
        to_airport=Chennai,
        type=boeing737,
        departure_time=datetime.time(hour=8, minute=0, second=0),
        arrival_time=datetime.time(hour=9, minute=30, second=0),
        day=tuesdaySchedule,
        distance=500
    )
    HyderabadtoChennaiOnTuesday.save()

    ChennaitoHyderabadOnTuesday = Trip(
        from_airport=Chennai,
        to_airport=Hyderabad,
        type=boeing737,
        departure_time=datetime.time(hour=11, minute=0, second=0),
        arrival_time=datetime.time(hour=12, minute=30, second=0),
        day=tuesdaySchedule,
        distance=500
    )
    ChennaitoHyderabadOnTuesday.save()

    #   Trips on Wednesday --------------------------------------------------

    HyderabadtoMumbaiOnWednesday = Trip(
        from_airport=Hyderabad,
        to_airport=Mumbai,
        type=boeing747,
        departure_time=datetime.time(hour=10, minute=0, second=0),
        arrival_time=datetime.time(hour=11, minute=45, second=0),
        day=wednesdaySchedule,
        distance=620
    )
    HyderabadtoMumbaiOnWednesday.save()

    MumbaitoHyderabadOnWednesday = Trip(
        from_airport=Mumbai,
        to_airport=Hyderabad,
        type=boeing747,
        departure_time=datetime.time(hour=13, minute=0, second=0),
        arrival_time=datetime.time(hour=14, minute=45, second=0),
        day=wednesdaySchedule,
        distance=620
    )
    MumbaitoHyderabadOnWednesday.save()

    DelhitoMumbaiOnWednesday = Trip(
        from_airport=Delhi,
        to_airport=Mumbai,
        type=boeing747,
        departure_time=datetime.time(hour=14, minute=0, second=0),
        arrival_time=datetime.time(hour=16, minute=30, second=0),
        day=wednesdaySchedule,
        distance=1200
    )
    DelhitoMumbaiOnWednesday.save()

    MumbaitoDelhiOnWednesday = Trip(
        from_airport=Mumbai,
        to_airport=Delhi,
        type=boeing747,
        departure_time=datetime.time(hour=17, minute=0, second=0),
        arrival_time=datetime.time(hour=19, minute=30, second=0),
        day=wednesdaySchedule,
        distance=1200
    )
    MumbaitoDelhiOnWednesday.save()

    HyderabadtoDelhiOnWednesday = Trip(
        from_airport=Hyderabad,
        to_airport=Delhi,
        type=boeing747,
        departure_time=datetime.time(hour=12, minute=0, second=0),
        arrival_time=datetime.time(hour=14, minute=30, second=0),
        day=wednesdaySchedule,
        distance=1300
    )
    HyderabadtoDelhiOnWednesday.save()

    DelhitoHyderabadOnWednesday = Trip(
        from_airport=Delhi,
        to_airport=Hyderabad,
        type=boeing747,
        departure_time=datetime.time(hour=16, minute=0, second=0),
        arrival_time=datetime.time(hour=18, minute=30, second=0),
        day=wednesdaySchedule,
        distance=1300
    )
    DelhitoHyderabadOnWednesday.save()

    HyderabadtoBangaloreOnWednesday = Trip(
        from_airport=Hyderabad,
        to_airport=Bangalore,
        type=boeing787,
        departure_time=datetime.time(hour=10, minute=0, second=0),
        arrival_time=datetime.time(hour=11, minute=15, second=0),
        day=wednesdaySchedule,
        distance=450
    )
    HyderabadtoBangaloreOnWednesday.save()

    BangaloretoHyderabadOnWednesday = Trip(
        from_airport=Bangalore,
        to_airport=Hyderabad,
        type=boeing787,
        departure_time=datetime.time(hour=12, minute=30, second=0),
        arrival_time=datetime.time(hour=13, minute=45, second=0),
        day=wednesdaySchedule,
        distance=450
    )
    BangaloretoHyderabadOnWednesday.save()

    HyderabadtoKolkataOnWednesday = Trip(
        from_airport=Hyderabad,
        to_airport=Kolkata,
        type=boeing737,
        departure_time=datetime.time(hour=17, minute=0, second=0),
        arrival_time=datetime.time(hour=19, minute=30, second=0),
        day=wednesdaySchedule,
        distance=1200
    )
    HyderabadtoKolkataOnWednesday.save()

    KolkatatoHyderabadOnWednesday = Trip(
        from_airport=Kolkata,
        to_airport=Hyderabad,
        type=boeing737,
        departure_time=datetime.time(hour=21, minute=0, second=0),
        arrival_time=datetime.time(hour=23, minute=30, second=0),
        day=wednesdaySchedule,
        distance=1200
    )
    KolkatatoHyderabadOnWednesday.save()

    HyderabadtoChennaiOnWednesday = Trip(
        from_airport=Hyderabad,
        to_airport=Chennai,
        type=boeing737,
        departure_time=datetime.time(hour=8, minute=0, second=0),
        arrival_time=datetime.time(hour=9, minute=30, second=0),
        day=wednesdaySchedule,
        distance=500
    )
    HyderabadtoChennaiOnWednesday.save()

    ChennaitoHyderabadOnWednesday = Trip(
        from_airport=Chennai,
        to_airport=Hyderabad,
        type=boeing737,
        departure_time=datetime.time(hour=11, minute=0, second=0),
        arrival_time=datetime.time(hour=12, minute=30, second=0),
        day=wednesdaySchedule,
        distance=500
    )
    ChennaitoHyderabadOnWednesday.save()

    #   Trips on Thursday ---------------------------------------------------

    HyderabadtoMumbaiOnThursday = Trip(
        from_airport=Hyderabad,
        to_airport=Mumbai,
        type=boeing747,
        departure_time=datetime.time(hour=10, minute=0, second=0),
        arrival_time=datetime.time(hour=11, minute=45, second=0),
        day=thursdaySchedule,
        distance=620
    )
    HyderabadtoMumbaiOnThursday.save()

    MumbaitoHyderabadOnThursday = Trip(
        from_airport=Mumbai,
        to_airport=Hyderabad,
        type=boeing747,
        departure_time=datetime.time(hour=13, minute=0, second=0),
        arrival_time=datetime.time(hour=14, minute=45, second=0),
        day=thursdaySchedule,
        distance=620
    )
    MumbaitoHyderabadOnThursday.save()

    DelhitoMumbaiOnThursday = Trip(
        from_airport=Delhi,
        to_airport=Mumbai,
        type=boeing747,
        departure_time=datetime.time(hour=14, minute=0, second=0),
        arrival_time=datetime.time(hour=16, minute=30, second=0),
        day=thursdaySchedule,
        distance=1200
    )
    DelhitoMumbaiOnThursday.save()

    MumbaitoDelhiOnThursday = Trip(
        from_airport=Mumbai,
        to_airport=Delhi,
        type=boeing747,
        departure_time=datetime.time(hour=17, minute=0, second=0),
        arrival_time=datetime.time(hour=19, minute=30, second=0),
        day=thursdaySchedule,
        distance=1200
    )
    MumbaitoDelhiOnThursday.save()

    HyderabadtoDelhiOnThursday = Trip(
        from_airport=Hyderabad,
        to_airport=Delhi,
        type=boeing747,
        departure_time=datetime.time(hour=12, minute=0, second=0),
        arrival_time=datetime.time(hour=14, minute=30, second=0),
        day=thursdaySchedule,
        distance=1300
    )
    HyderabadtoDelhiOnThursday.save()

    DelhitoHyderabadOnThursday = Trip(
        from_airport=Delhi,
        to_airport=Hyderabad,
        type=boeing747,
        departure_time=datetime.time(hour=16, minute=0, second=0),
        arrival_time=datetime.time(hour=18, minute=30, second=0),
        day=thursdaySchedule,
        distance=1300
    )
    DelhitoHyderabadOnThursday.save()

    HyderabadtoBangaloreOnThursday = Trip(
        from_airport=Hyderabad,
        to_airport=Bangalore,
        type=boeing787,
        departure_time=datetime.time(hour=10, minute=0, second=0),
        arrival_time=datetime.time(hour=11, minute=15, second=0),
        day=thursdaySchedule,
        distance=450
    )
    HyderabadtoBangaloreOnThursday.save()

    BangaloretoHyderabadOnThursday = Trip(
        from_airport=Bangalore,
        to_airport=Hyderabad,
        type=boeing787,
        departure_time=datetime.time(hour=12, minute=30, second=0),
        arrival_time=datetime.time(hour=13, minute=45, second=0),
        day=thursdaySchedule,
        distance=450
    )
    BangaloretoHyderabadOnThursday.save()

    HyderabadtoKolkataOnThursday = Trip(
        from_airport=Hyderabad,
        to_airport=Kolkata,
        type=boeing737,
        departure_time=datetime.time(hour=17, minute=0, second=0),
        arrival_time=datetime.time(hour=19, minute=30, second=0),
        day=thursdaySchedule,
        distance=1200
    )
    HyderabadtoKolkataOnThursday.save()

    KolkatatoHyderabadOnThursday = Trip(
        from_airport=Kolkata,
        to_airport=Hyderabad,
        type=boeing737,
        departure_time=datetime.time(hour=21, minute=0, second=0),
        arrival_time=datetime.time(hour=23, minute=30, second=0),
        day=thursdaySchedule,
        distance=1200
    )
    KolkatatoHyderabadOnThursday.save()

    HyderabadtoChennaiOnThursday = Trip(
        from_airport=Hyderabad,
        to_airport=Chennai,
        type=boeing737,
        departure_time=datetime.time(hour=8, minute=0, second=0),
        arrival_time=datetime.time(hour=9, minute=30, second=0),
        day=thursdaySchedule,
        distance=500
    )
    HyderabadtoChennaiOnThursday.save()

    ChennaitoHyderabadOnThursday = Trip(
        from_airport=Chennai,
        to_airport=Hyderabad,
        type=boeing737,
        departure_time=datetime.time(hour=11, minute=0, second=0),
        arrival_time=datetime.time(hour=12, minute=30, second=0),
        day=thursdaySchedule,
        distance=500
    )
    ChennaitoHyderabadOnThursday.save()

    #   Trips on Friday -----------------------------------------------------

    HyderabadtoMumbaiOnFriday = Trip(
        from_airport=Hyderabad,
        to_airport=Mumbai,
        type=boeing747,
        departure_time=datetime.time(hour=10, minute=0, second=0),
        arrival_time=datetime.time(hour=11, minute=45, second=0),
        day=fridaySchedule,
        distance=620
    )
    HyderabadtoMumbaiOnFriday.save()

    MumbaitoHyderabadOnFriday = Trip(
        from_airport=Mumbai,
        to_airport=Hyderabad,
        type=boeing747,
        departure_time=datetime.time(hour=13, minute=0, second=0),
        arrival_time=datetime.time(hour=14, minute=45, second=0),
        day=fridaySchedule,
        distance=620
    )
    MumbaitoHyderabadOnFriday.save()

    DelhitoMumbaiOnFriday = Trip(
        from_airport=Delhi,
        to_airport=Mumbai,
        type=boeing747,
        departure_time=datetime.time(hour=14, minute=0, second=0),
        arrival_time=datetime.time(hour=16, minute=30, second=0),
        day=fridaySchedule,
        distance=1200
    )
    DelhitoMumbaiOnFriday.save()

    MumbaitoDelhiOnFriday = Trip(
        from_airport=Mumbai,
        to_airport=Delhi,
        type=boeing747,
        departure_time=datetime.time(hour=17, minute=0, second=0),
        arrival_time=datetime.time(hour=19, minute=30, second=0),
        day=fridaySchedule,
        distance=1200
    )
    MumbaitoDelhiOnFriday.save()

    HyderabadtoDelhiOnFriday = Trip(
        from_airport=Hyderabad,
        to_airport=Delhi,
        type=boeing747,
        departure_time=datetime.time(hour=12, minute=0, second=0),
        arrival_time=datetime.time(hour=14, minute=30, second=0),
        day=fridaySchedule,
        distance=1300
    )
    HyderabadtoDelhiOnFriday.save()

    DelhitoHyderabadOnFriday = Trip(
        from_airport=Delhi,
        to_airport=Hyderabad,
        type=boeing747,
        departure_time=datetime.time(hour=16, minute=0, second=0),
        arrival_time=datetime.time(hour=18, minute=30, second=0),
        day=fridaySchedule,
        distance=1300
    )
    DelhitoHyderabadOnFriday.save()

    HyderabadtoBangaloreOnFriday = Trip(
        from_airport=Hyderabad,
        to_airport=Bangalore,
        type=boeing787,
        departure_time=datetime.time(hour=10, minute=0, second=0),
        arrival_time=datetime.time(hour=11, minute=15, second=0),
        day=fridaySchedule,
        distance=450
    )
    HyderabadtoBangaloreOnFriday.save()

    BangaloretoHyderabadOnFriday = Trip(
        from_airport=Bangalore,
        to_airport=Hyderabad,
        type=boeing787,
        departure_time=datetime.time(hour=12, minute=30, second=0),
        arrival_time=datetime.time(hour=13, minute=45, second=0),
        day=fridaySchedule,
        distance=450
    )
    BangaloretoHyderabadOnFriday.save()

    HyderabadtoKolkataOnFriday = Trip(
        from_airport=Hyderabad,
        to_airport=Kolkata,
        type=boeing737,
        departure_time=datetime.time(hour=17, minute=0, second=0),
        arrival_time=datetime.time(hour=19, minute=30, second=0),
        day=fridaySchedule,
        distance=1200
    )
    HyderabadtoKolkataOnFriday.save()

    KolkatatoHyderabadOnFriday = Trip(
        from_airport=Kolkata,
        to_airport=Hyderabad,
        type=boeing737,
        departure_time=datetime.time(hour=21, minute=0, second=0),
        arrival_time=datetime.time(hour=23, minute=30, second=0),
        day=fridaySchedule,
        distance=1200
    )
    KolkatatoHyderabadOnFriday.save()

    HyderabadtoChennaiOnFriday = Trip(
        from_airport=Hyderabad,
        to_airport=Chennai,
        type=boeing737,
        departure_time=datetime.time(hour=8, minute=0, second=0),
        arrival_time=datetime.time(hour=9, minute=30, second=0),
        day=fridaySchedule,
        distance=500
    )
    HyderabadtoChennaiOnFriday.save()

    ChennaitoHyderabadOnFriday = Trip(
        from_airport=Chennai,
        to_airport=Hyderabad,
        type=boeing737,
        departure_time=datetime.time(hour=11, minute=0, second=0),
        arrival_time=datetime.time(hour=12, minute=30, second=0),
        day=fridaySchedule,
        distance=500
    )
    ChennaitoHyderabadOnFriday.save()

    #   Trips on Saturday ---------------------------------------------------

    HyderabadtoMumbaiOnSaturday = Trip(
        from_airport=Hyderabad,
        to_airport=Mumbai,
        type=boeing747,
        departure_time=datetime.time(hour=10, minute=0, second=0),
        arrival_time=datetime.time(hour=11, minute=45, second=0),
        day=saturdaySchedule,
        distance=620
    )
    HyderabadtoMumbaiOnSaturday.save()

    MumbaitoHyderabadOnSaturday = Trip(
        from_airport=Mumbai,
        to_airport=Hyderabad,
        type=boeing747,
        departure_time=datetime.time(hour=13, minute=0, second=0),
        arrival_time=datetime.time(hour=14, minute=45, second=0),
        day=saturdaySchedule,
        distance=620
    )
    MumbaitoHyderabadOnSaturday.save()

    DelhitoMumbaiOnSaturday = Trip(
        from_airport=Delhi,
        to_airport=Mumbai,
        type=boeing747,
        departure_time=datetime.time(hour=14, minute=0, second=0),
        arrival_time=datetime.time(hour=16, minute=30, second=0),
        day=saturdaySchedule,
        distance=1200
    )
    DelhitoMumbaiOnSaturday.save()

    MumbaitoDelhiOnSaturday = Trip(
        from_airport=Mumbai,
        to_airport=Delhi,
        type=boeing747,
        departure_time=datetime.time(hour=17, minute=0, second=0),
        arrival_time=datetime.time(hour=19, minute=30, second=0),
        day=saturdaySchedule,
        distance=1200
    )
    MumbaitoDelhiOnSaturday.save()

    HyderabadtoDelhiOnSaturday = Trip(
        from_airport=Hyderabad,
        to_airport=Delhi,
        type=boeing747,
        departure_time=datetime.time(hour=12, minute=0, second=0),
        arrival_time=datetime.time(hour=14, minute=30, second=0),
        day=saturdaySchedule,
        distance=1300
    )
    HyderabadtoDelhiOnSaturday.save()

    DelhitoHyderabadOnSaturday = Trip(
        from_airport=Delhi,
        to_airport=Hyderabad,
        type=boeing747,
        departure_time=datetime.time(hour=16, minute=0, second=0),
        arrival_time=datetime.time(hour=18, minute=30, second=0),
        day=saturdaySchedule,
        distance=1300
    )
    DelhitoHyderabadOnSaturday.save()

    HyderabadtoBangaloreOnSaturday = Trip(
        from_airport=Hyderabad,
        to_airport=Bangalore,
        type=boeing787,
        departure_time=datetime.time(hour=10, minute=0, second=0),
        arrival_time=datetime.time(hour=11, minute=15, second=0),
        day=saturdaySchedule,
        distance=450
    )
    HyderabadtoBangaloreOnSaturday.save()

    BangaloretoHyderabadOnSaturday = Trip(
        from_airport=Bangalore,
        to_airport=Hyderabad,
        type=boeing787,
        departure_time=datetime.time(hour=12, minute=30, second=0),
        arrival_time=datetime.time(hour=13, minute=45, second=0),
        day=saturdaySchedule,
        distance=450
    )
    BangaloretoHyderabadOnSaturday.save()

    HyderabadtoKolkataOnSaturday = Trip(
        from_airport=Hyderabad,
        to_airport=Kolkata,
        type=boeing737,
        departure_time=datetime.time(hour=17, minute=0, second=0),
        arrival_time=datetime.time(hour=19, minute=30, second=0),
        day=saturdaySchedule,
        distance=1200
    )
    HyderabadtoKolkataOnSaturday.save()

    KolkatatoHyderabadOnSaturday = Trip(
        from_airport=Kolkata,
        to_airport=Hyderabad,
        type=boeing737,
        departure_time=datetime.time(hour=21, minute=0, second=0),
        arrival_time=datetime.time(hour=23, minute=30, second=0),
        day=saturdaySchedule,
        distance=1200
    )
    KolkatatoHyderabadOnSaturday.save()

    HyderabadtoChennaiOnSaturday = Trip(
        from_airport=Hyderabad,
        to_airport=Chennai,
        type=boeing737,
        departure_time=datetime.time(hour=8, minute=0, second=0),
        arrival_time=datetime.time(hour=9, minute=30, second=0),
        day=saturdaySchedule,
        distance=500
    )
    HyderabadtoChennaiOnSaturday.save()

    ChennaitoHyderabadOnSaturday = Trip(
        from_airport=Chennai,
        to_airport=Hyderabad,
        type=boeing737,
        departure_time=datetime.time(hour=11, minute=0, second=0),
        arrival_time=datetime.time(hour=12, minute=30, second=0),
        day=saturdaySchedule,
        distance=500
    )
    ChennaitoHyderabadOnSaturday.save()

    #   Trips on Sunday -----------------------------------------------------

    HyderabadtoMumbaiOnSunday = Trip(
        from_airport=Hyderabad,
        to_airport=Mumbai,
        type=boeing747,
        departure_time=datetime.time(hour=10, minute=0, second=0),
        arrival_time=datetime.time(hour=11, minute=45, second=0),
        day=sundaySchedule,
        distance=620
    )
    HyderabadtoMumbaiOnSunday.save()

    MumbaitoHyderabadOnSunday = Trip(
        from_airport=Mumbai,
        to_airport=Hyderabad,
        type=boeing747,
        departure_time=datetime.time(hour=13, minute=0, second=0),
        arrival_time=datetime.time(hour=14, minute=45, second=0),
        day=sundaySchedule,
        distance=620
    )
    MumbaitoHyderabadOnSunday.save()

    DelhitoMumbaiOnSunday = Trip(
        from_airport=Delhi,
        to_airport=Mumbai,
        type=boeing747,
        departure_time=datetime.time(hour=14, minute=0, second=0),
        arrival_time=datetime.time(hour=16, minute=30, second=0),
        day=sundaySchedule,
        distance=1200
    )
    DelhitoMumbaiOnSunday.save()

    MumbaitoDelhiOnSunday = Trip(
        from_airport=Mumbai,
        to_airport=Delhi,
        type=boeing747,
        departure_time=datetime.time(hour=17, minute=0, second=0),
        arrival_time=datetime.time(hour=19, minute=30, second=0),
        day=sundaySchedule,
        distance=1200
    )
    MumbaitoDelhiOnSunday.save()

    HyderabadtoDelhiOnSunday = Trip(
        from_airport=Hyderabad,
        to_airport=Delhi,
        type=boeing747,
        departure_time=datetime.time(hour=12, minute=0, second=0),
        arrival_time=datetime.time(hour=14, minute=30, second=0),
        day=sundaySchedule,
        distance=1300
    )
    HyderabadtoDelhiOnSunday.save()

    DelhitoHyderabadOnSunday = Trip(
        from_airport=Delhi,
        to_airport=Hyderabad,
        type=boeing747,
        departure_time=datetime.time(hour=16, minute=0, second=0),
        arrival_time=datetime.time(hour=18, minute=30, second=0),
        day=sundaySchedule,
        distance=1300
    )
    DelhitoHyderabadOnSunday.save()

    HyderabadtoBangaloreOnSunday = Trip(
        from_airport=Hyderabad,
        to_airport=Bangalore,
        type=boeing787,
        departure_time=datetime.time(hour=10, minute=0, second=0),
        arrival_time=datetime.time(hour=11, minute=15, second=0),
        day=sundaySchedule,
        distance=450
    )
    HyderabadtoBangaloreOnSunday.save()

    BangaloretoHyderabadOnSunday = Trip(
        from_airport=Bangalore,
        to_airport=Hyderabad,
        type=boeing787,
        departure_time=datetime.time(hour=12, minute=30, second=0),
        arrival_time=datetime.time(hour=13, minute=45, second=0),
        day=sundaySchedule,
        distance=450
    )
    BangaloretoHyderabadOnSunday.save()

    HyderabadtoKolkataOnSunday = Trip(
        from_airport=Hyderabad,
        to_airport=Kolkata,
        type=boeing737,
        departure_time=datetime.time(hour=17, minute=0, second=0),
        arrival_time=datetime.time(hour=19, minute=30, second=0),
        day=sundaySchedule,
        distance=1200
    )
    HyderabadtoKolkataOnSunday.save()

    KolkatatoHyderabadOnSunday = Trip(
        from_airport=Kolkata,
        to_airport=Hyderabad,
        type=boeing737,
        departure_time=datetime.time(hour=21, minute=0, second=0),
        arrival_time=datetime.time(hour=23, minute=30, second=0),
        day=sundaySchedule,
        distance=1200
    )
    KolkatatoHyderabadOnSunday.save()

    HyderabadtoChennaiOnSunday = Trip(
        from_airport=Hyderabad,
        to_airport=Chennai,
        type=boeing737,
        departure_time=datetime.time(hour=8, minute=0, second=0),
        arrival_time=datetime.time(hour=9, minute=30, second=0),
        day=sundaySchedule,
        distance=500
    )
    HyderabadtoChennaiOnSunday.save()

    ChennaitoHyderabadOnSunday = Trip(
        from_airport=Chennai,
        to_airport=Hyderabad,
        type=boeing737,
        departure_time=datetime.time(hour=11, minute=0, second=0),
        arrival_time=datetime.time(hour=12, minute=30, second=0),
        day=sundaySchedule,
        distance=500
    )
    ChennaitoHyderabadOnSunday.save()

    print('file completely ran\n')

#   All Trips for a week are created.
