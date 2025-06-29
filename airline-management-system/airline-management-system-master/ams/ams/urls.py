from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

# app_name = 'ams1'

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^$', views.homepage, name="homepage"),
    url(r'^help/', views.help_main, name="help"),
    # url(r'^about/', views.about, name="about"),
    url(r'^user_accounts/', include('user_accounts.urls')),
    url(r'^passengers/', include('passengers.urls')),
    url(r'^managers/', include('managers.urls')),
    url(r'^airlines/', include('airlines.urls')),
    url(r'^who-we-are/', views.creators, name="who_we_are")
]

urlpatterns += staticfiles_urlpatterns()
