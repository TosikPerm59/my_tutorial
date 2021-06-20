from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index_djtut(reqest):
    return render(reqest, 'django_tutorial/index.html')
