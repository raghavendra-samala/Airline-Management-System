from django.conf.urls import url, include
from . import views

app_name = 'passengers'

urlpatterns = [
    url(r'^$', views.passenger_homepage, name="passenger"),
    url(r'^book_ticket/', views.book_ticket, name="book"),
    url(r'^add_balance/', views.add_balance, name="balance"),
    url(r'^add_details/', views.add_details, name="details"),
    url(r'^upcoming_trips/', views.see_tickets, name="trips"),
    url(r'^search/', views.search_flights, name="search"),
    url(r'^flight/(?P<slug>[\w-]+)/$', views.flight_detail, name="flight"),
    url(r'^(?P<slug>[\w-]+)/$', views.ticket_detail, name="ticket"),
    url(r'^mod_ticket/(?P<slug>[\w-]+)/$', views.modify_ticket, name='modify_ticket'),
    url(r'^del_ticket/(?P<slug>[\w-]+)/$', views.del_ticket, name='del_ticket'),
    url(r'^details/(?P<slug>[\w-]+)/$', views.details_of_flight, name='detail'),
    url(r'^choose_seat/(?P<slug>[\w-]+)/$', views.choose_seat, name='choose_seat'),
]
