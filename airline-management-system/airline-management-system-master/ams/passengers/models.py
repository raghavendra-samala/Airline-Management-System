from django.db import models
from django.conf import settings
from airlines.models import AirplaneType
from user_accounts.models import Passenger, User


# Create your models here
class Tickets(models.Model):
    pnr = models.CharField(max_length=100, null=True)
    booking_id = models.CharField(max_length=100, null=True)
    slug = models.SlugField(null=True)
    from_station = models.CharField(max_length=100, null=True)
    to_station = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    booking_date = models.DateField(auto_now_add=True, null=True)
    passenger_name = models.CharField(max_length=100, blank=True)
    passenger_age = models.IntegerField(default=0)
    passenger_gender = models.CharField(max_length=10, blank=True)
    ticket_holder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                      related_name='ticket_holder')
    journey_date = models.DateField(null=True)
    seat_number = models.IntegerField(null=True)
    seat_type = models.CharField(max_length=100, null=True)
    fare = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        # user = Passenger.objects.get(user_id=self.ticket_holder.user_id)
        username = str(self.ticket_holder)
        user = User.objects.get(username=username)
        user.balance -= self.fare
        user.save()
        # self.ticket_holder.balance -= self.fare
        self.ticket_holder = user
        # print('balane : '+str(user.balance))
        self.slug = self.booking_id + self.seat_type[0] + str(self.seat_number)
        self.pnr = self.slug
        super(Tickets, self).save(*args, **kwargs)
