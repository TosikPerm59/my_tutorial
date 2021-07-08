from django import db
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django_tutorial.models import *


def index_djtut(reqest):
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'title': 'Учебные материалы'
    }

    return render(reqest, 'django_tutorial/index.html',  context=context)


