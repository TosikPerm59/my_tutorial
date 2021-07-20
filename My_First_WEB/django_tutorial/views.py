from django import db
from django.shortcuts import render

from django_tutorial.Templates.temlatetags.django_tutorial_tags import get_articles, links_list
from django_tutorial.models import *

def index_djtut(reqest):
    context = {
        'articles': get_articles,
        'title': 'Учебные материалы'
    }

    return render(reqest, 'django_tutorial/index.html',  context=context)


def show_article(reqest, article_id):
    context = {
        'articles': get_articles,
        'article_id': article_id,
        'title': 'Учебные материалы',
        'links': links_list(article_id)
    }

    return render(reqest, 'django_tutorial/index.html', context=context)
