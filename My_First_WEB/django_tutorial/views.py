
from django.shortcuts import render

from django_tutorial.Templates.temlatetags.django_tutorial_tags import *




def index_djtut(request):
    context = {
        'articles': get_articles,
        'title': 'Учебные материалы'
    }

    return render(request, 'django_tutorial/index.html',  context=context)


def show_article(request, article_id):
    context = {
        'articles': get_articles,
        'article_id': article_id,
        'title': 'Учебные материалы',
        'links': links_list(article_id)
    }

    return render(request, 'django_tutorial/index.html', context=context)


def search_results(request):
    search_query = request.GET.get('search_string')
    if search_query:
        search_words = search_query.split()
        search_res_in_name = Article.objects.filter(name__contains=search_words[0] or search_words[1] or search_words[2])
        search_res_in_content = Article.objects.filter(content__contains=search_words[0] or search_words[1] or search_words[2])

    else:
        context = {
            'articles': get_articles,
            'title': 'Результат поиска'
        }
        return render(request, 'django_tutorial/search_result.html', context=context)


    context = {
        'articles': get_articles,
        'title': 'Результат поиска',
        'search_words': search_query,
        'search_res_in_name': search_res_in_name,
        'search_res_in_content': search_res_in_content,
    }

    return render(request, 'django_tutorial/search_result.html', context=context)







