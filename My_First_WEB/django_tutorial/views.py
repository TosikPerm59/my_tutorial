from django import db
from django.shortcuts import render
from django_tutorial.models import *


def index_djtut(reqest):
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'title': 'Учебные материалы'
    }

    return render(reqest, 'django_tutorial/index.html',  context=context)


def show_article(reqest, article_id):
    articles = Article.objects.all()
    # art = Article.objects.filter(pk=article_id)
    context = {
        'articles': articles,
        'article_id': article_id,
        'title': 'Учебные материалы'
    }

    return render(reqest, 'django_tutorial/index.html', context=context)
