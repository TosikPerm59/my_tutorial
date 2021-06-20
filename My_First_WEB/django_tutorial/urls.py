from django.urls import path

from django_tutorial.views import *

urlpatterns = [
    path('', index_djtut, name='djtut')
]