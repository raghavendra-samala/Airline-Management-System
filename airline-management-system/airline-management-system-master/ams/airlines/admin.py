from django.contrib import admin

from .models import Airport, Flight, Schedule, EconomyClass, BusinessClass, AirplaneType, FirstClass, Trip, Airline

# Register your models here.

admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Trip)
admin.site.register(Schedule)
admin.site.register(EconomyClass)
admin.site.register(BusinessClass)
admin.site.register(FirstClass)
admin.site.register(AirplaneType)
admin.site.register(Airline)

