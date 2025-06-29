from django.db import models
from datetime import timedelta, date
import re
from django.template.defaultfilters import slugify


def unique_slugify(instance, value, slug_field_name='slug', queryset=None,
                   slug_separator='-'):
    """
    Calculates and stores a unique slug of ``value`` for an instance.

    ``slug_field_name`` should be a string matching the name of the field to
    store the slug in (and the field to check against for uniqueness).

    ``queryset`` usually doesn't need to be explicitly provided - it'll default
    to using the ``.all()`` queryset from the model's default manager.
    """
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    # Sort out the initial slug, limiting its length if necessary.
    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    # Create the queryset if one wasn't explicitly provided and exclude the
    # current instance from the queryset.
    if queryset is None:
        queryset = instance.__class__._default_manager.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    # Find a unique slug. If one matches, at '-2' to the end and try again
    # (then '-3', etc).
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = '%s%s' % (slug_separator, next)
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[:slug_len-len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = '%s%s' % (slug, end)
        next += 1

    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator='-'):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.

    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    separator = separator or ''
    if separator == '-' or not separator:
        re_sep = '-'
    else:
        re_sep = '(?:-|%s)' % re.escape(separator)
    # Remove multiple instances and if an alternate separator is provided,
    # replace the default '-' separator.
    if separator != re_sep:
        value = re.sub('%s+' % re_sep, separator, value)
    # Remove separator from the beginning and end of the slug.
    if separator:
        if separator != '-':
            re_sep = re.escape(separator)
        value = re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
    return value


# Create your models here.

class Airport(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class SeatType(models.Model):
    # name = models.CharField(max_length=20,null=True)
    seat = models.PositiveIntegerField(null=True)
    load_factor = models.FloatField(null=True)

    class Meta:
        abstract = True


class EconomyClass(SeatType):
    pass


class BusinessClass(SeatType):
    pass


class FirstClass(SeatType):
    pass


class Airline(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class AirplaneType(models.Model):
    airplane_type = models.CharField(max_length=20, null=True)
    first_class = models.ForeignKey(FirstClass, on_delete=models.CASCADE, null=True, related_name='first_class')
    economy_class = models.ForeignKey(EconomyClass, on_delete=models.CASCADE, null=True, related_name='economy_class')
    business_class = models.ForeignKey(BusinessClass, on_delete=models.CASCADE, null=True,
                                       related_name='business_class')
    cost_per_km = models.FloatField(null=True)
    fare_per_km = models.FloatField(null=True)
    basic_cost = models.FloatField(null=True)
    count = models.IntegerField(default=0)

    # capacity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.airplane_type


class Schedule(models.Model):
    day = models.CharField(max_length=10, null=True)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.day


class Flight(models.Model):
    distance = models.IntegerField(null=True)
    extra_requests = models.IntegerField(default=0)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, null=True)
    from_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, null=True, related_name='fromAirport')
    to_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, null=True, related_name='toAirport')
    type = models.ForeignKey(AirplaneType, on_delete=models.CASCADE, null=True, related_name='planeType')
    flight_id = models.CharField(max_length=100, null=True)
    departure_time = models.TimeField(null=True)
    arrival_time = models.TimeField(null=True)
    journey_date = models.DateField(null=True)
    slug = models.SlugField(null=True)
    first_class_seats = models.IntegerField(default=0)
    business_class_seats = models.IntegerField(default=0)
    economy_class_seats = models.IntegerField(default=0)
    first_class_occupancy = models.CharField(max_length=200, default="", blank=True)
    business_class_occupancy = models.CharField(max_length=200, default="", blank=True)
    economy_class_occupancy = models.CharField(max_length=200, default="", blank=True)
    first_class_occupancy_number = models.IntegerField(default=0)
    business_class_occupancy_number = models.IntegerField(default=0)
    economy_class_occupancy_number = models.IntegerField(default=0)
    profits = models.IntegerField(default=0)
    first_class_fare = models.IntegerField(default=0)
    business_class_fare = models.IntegerField(default=0)
    economy_class_fare = models.IntegerField(default=0)

    def __str__(self):
        return self.flight_id

    def __init__(self, *args, **kwargs):
        super(Flight, self).__init__(*args, **kwargs)
        a = self.first_class_seats
        b = self.business_class_seats
        c = self.economy_class_seats
        list1 = "0" * a
        list2 = "0" * b
        list3 = "0" * c
        if self.first_class_occupancy == "":
            self.first_class_occupancy = list1
        if self.business_class_occupancy == "":
            self.business_class_occupancy = list2
        if self.economy_class_occupancy == "":
            self.economy_class_occupancy = list3
        if self.first_class_fare == 0:
            self.first_class_fare = self.type.basic_cost + self.type.fare_per_km * self.distance * self.type.first_class.load_factor
        if self.business_class_fare == 0:
            self.business_class_fare = self.type.basic_cost + self.type.fare_per_km * self.distance * self.type.business_class.load_factor
        if self.economy_class_fare == 0:
            self.economy_class_fare = self.type.basic_cost + self.type.fare_per_km * self.distance * self.type.economy_class.load_factor
        if self.profits == 0:
            self.profits -= self.distance * self.type.cost_per_km

    def save(self, *args, **kwargs):
        slug = self.from_airport.name[0] + self.to_airport.name[0] + str(self.journey_date)
        unique_slugify(self, slug)
        self.flight_id = self.slug
        super(Flight, self).save(*args, **kwargs)


class Trip(models.Model):
    from_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, null=True, related_name='from_airport')
    to_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, null=True, related_name='to_airport')
    type = models.ForeignKey(AirplaneType, on_delete=models.CASCADE, null=True, related_name='type')
    departure_time = models.TimeField(null=True)
    arrival_time = models.TimeField(null=True)
    day = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True, related_name='Schedule_day')
    distance = models.PositiveIntegerField(null=True)

    def __str__(self):
        return str(self.day) + self.from_airport.name[0] + self.to_airport.name[0]

    def next_weekday(self, d, weekday):
        days_ahead = weekday - d.weekday()
        if days_ahead <= 0:  # Target day already happened this week
            days_ahead += 7
        return d + timedelta(days_ahead)

    def save(self, *args, **kwargs):
        week = timedelta(days=7)
        today = date.today()

        if self.day.day == 'Monday':
            day1 = 0
        if self.day.day == 'Tuesday':
            day1 = 1
        if self.day.day == 'Wednesday':
            day1 = 2
        if self.day.day == 'Thursday':
            day1 = 3
        if self.day.day == 'Friday':
            day1 = 4
        if self.day.day == 'Saturday':
            day1 = 5
        if self.day.day == 'Sunday':
            day1 = 6

        day = self.next_weekday(today, day1)

        f1 = Flight(
            airline=self.day.airline,
            from_airport=self.from_airport,
            to_airport=self.to_airport,
            type=self.type,
            arrival_time=self.arrival_time,
            departure_time=self.departure_time,
            distance=self.distance,
            journey_date=day,
            flight_id=self.from_airport.name[0] + self.to_airport.name[0] + str(day),
            slug=self.from_airport.name[0] + self.to_airport.name[0] + str(day),
            first_class_seats=self.type.first_class.seat,
            economy_class_seats=self.type.economy_class.seat,
            business_class_seats=self.type.business_class.seat,
        )
        day += week
        f1.save()

        f2 = Flight(
            airline=self.day.airline,
            from_airport=self.from_airport,
            to_airport=self.to_airport,
            type=self.type,
            arrival_time=self.arrival_time,
            departure_time=self.departure_time,
            distance=self.distance,
            journey_date=day,
            flight_id=self.from_airport.name[0] + self.to_airport.name[0] + str(day),
            slug=self.from_airport.name[0] + self.to_airport.name[0] + str(day),
            first_class_seats=self.type.first_class.seat,
            economy_class_seats=self.type.economy_class.seat,
            business_class_seats=self.type.business_class.seat,
        )
        day += week
        f2.save()

        f3 = Flight(
            airline=self.day.airline,
            from_airport=self.from_airport,
            to_airport=self.to_airport,
            type=self.type,
            arrival_time=self.arrival_time,
            departure_time=self.departure_time,
            distance=self.distance,
            journey_date=day,
            flight_id=self.from_airport.name[0] + self.to_airport.name[0] + str(day),
            slug=self.from_airport.name[0] + self.to_airport.name[0] + str(day),
            first_class_seats=self.type.first_class.seat,
            economy_class_seats=self.type.economy_class.seat,
            business_class_seats=self.type.business_class.seat,
        )
        day += week
        f3.save()

        f4 = Flight(
            airline=self.day.airline,
            from_airport=self.from_airport,
            to_airport=self.to_airport,
            type=self.type,
            arrival_time=self.arrival_time,
            departure_time=self.departure_time,
            distance=self.distance,
            journey_date=day,
            flight_id=self.from_airport.name[0] + self.to_airport.name[0] + str(day),
            slug=self.from_airport.name[0] + self.to_airport.name[0] + str(day),
            first_class_seats=self.type.first_class.seat,
            economy_class_seats=self.type.economy_class.seat,
            business_class_seats=self.type.business_class.seat,
        )
        f4.save()
        super(Trip, self).save()

    def delete(self, *args, **kwargs):
        for flight in Flight.objects.all():
            week = timedelta(days=7)
            today = date.today()

            if self.day.day == 'Monday':
                day1 = 0
            if self.day.day == 'Tuesday':
                day1 = 1
            if self.day.day == 'Wednesday':
                day1 = 2
            if self.day.day == 'Thursday':
                day1 = 3
            if self.day.day == 'Friday':
                day1 = 4
            if self.day.day == 'Saturday':
                day1 = 5
            if self.day.day == 'Sunday':
                day1 = 6

            day2 = self.next_weekday(today, day1)
            day2 += week
            day3 = day2 + week
            day4 = day3 + week

            if flight.from_airport == self.from_airport and flight.to_airport == self.to_airport:
                if str(day2) == str(flight.journey_date) or str(day3) == str(flight.journey_date) or str(day4) == str(
                        flight.journey_date):
                    if flight.type == self.type:
                        if flight.arrival_time == self.arrival_time and flight.departure_time == self.departure_time:
                            flight.delete()

            super(Trip, self).delete()
