from django import template
from django_tutorial.models import *
# from django_tutorial.views import query





# def get_id_list():
#     print('началось получение листа айди')
#     global id_list
#     global id_list_example
#     global new_list_id
#     for article in Article.objects.all():
#         id_list_example.append(article.id)
#     print('получившаяся длина списка в БД=', len(id_list_example))
#     print('длина сохраненного списка=', len(id_list))
#     print('сохраненый список=', id_list)
#     print('вычитанный из базы список=', sorted(id_list_example))
#     if id_list != sorted(id_list_example):
#         print('списки оказались не равны')
#         new_list_id = True
#         id_list = sorted(id_list_example)
#         id_list_example = []
#         print('== сдесь должен обнулиться id_list_example ')
#         print('id_ex=', len(id_list_example))
#         print('id_list=', len(id_list))
#     elif len(id_list) == 0:
#         print('айди оказался пустым')
#         new_list_id = True
#         id_list = id_list_example
#         print('new_id=', len(id_list))
#         id_list_example = []
#         print('== сдесь должен обнулиться id_list_example ')
#         print('id_ex=', len(id_list_example))
#         print('id_list=', len(id_list))
#
#     else:
#         print('списки оказались равны')
#         new_list_id = False
#         id_list_example = []
#         print('== сдесь должен обнулиться id_list_example ')
#         print('id_ex=', len(id_list_example))
#         print('id_list=', len(id_list))
#     print('new_list_id=', new_list_id)
#     return new_list_id




def get_articles():
    article_data = Article.objects.all()

    return article_data


def links_list(element_id):
    link = str()
    links_l = []
    for example in get_articles():
        if example.id == element_id:
            links_l = example.links.split(';')
            return links_l




