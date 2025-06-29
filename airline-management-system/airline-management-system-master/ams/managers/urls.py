from django.conf.urls import url
from . import views

app_name = 'managers'

urlpatterns = [
    url(r'^$', views.manager_homepage, name="manager"),
    url(r'^check_occupancy/', views.check_occupancy, name="check"),
    url(r'^change_schedule/', views.change_schedule, name="change"),
    url(r'^get_profits/', views.get_profits, name="profit"),
    url(r'^add_flight/', views.add_flight, name="add"),
    url(r'^delete_flight/', views.delete_flight, name="delete"),
    url(r'^search/', views.search_flights, name="search"),
    url(r'^view_occupancy/',views.view_occupancy,name="view_occupancy"),
    url(r'^change_costs/', views.change_costs, name="costs"),
    url(r'^modify_costs/', views.modify_costs, name="modify"),
    url(r'^(?P<slug>[\w-]+)/$', views.del_flight, name="del"),
]
