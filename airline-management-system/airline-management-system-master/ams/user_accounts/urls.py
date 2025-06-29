from django.conf.urls import url
from . import views

app_name = 'user_accounts'

urlpatterns = [
    url(r'^$', views.choose_view, name="choose"),
    url(r'^passenger_signup/', views.PassengerSignup.as_view(), name="passenger_signup"),
    url(r'^manager_signup/', views.ManagerSignup.as_view(), name="manager_signup"),
    url(r'^login/', views.login_view, name="login"),
    url(r'^logout/', views.logout_view, name="logout"),
    url(r'^logout-confirm/', views.logout_confirm, name="logout_confirm")
]
