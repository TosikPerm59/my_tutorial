from django.urls import path

from amcarservice.views import *
from django_tutorial.views import *

urlpatterns = [
    path('', index_amcrsrs, name='amcrsrs'),
    path('station_staff/', station_staff, name='staff'),
    path('our_services/', our_services, name='our_services'),
    path('about/', about, name='about'),
    path('add_page/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('django_tutorial/', index_djtut, name='djtut'),
]