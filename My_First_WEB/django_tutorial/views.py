
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

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


def search_results(reqest):
    query = reqest.GET.get('search_string')
    context = {
        'articles': get_articles,
        'title': 'Результат поиска',
        'search_words': query
    }
    print(query)
    return render(reqest, 'django_tutorial/index.html', context=context)







