from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from amcarservice.models import *

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]


def index_amcrsrs(reqest):
    return render(reqest, 'Amcarservice/index.html', {'menu': menu, 'title': 'Главная страница'})


def about(reqest):
    return render(reqest, 'Amcarservice/about.html',  {'menu': menu, 'title': 'О сайте'})


def our_services(reqest):
    return render(reqest, 'Amcarservice/our_services.html', {'menu': menu, 'title': 'Наши услуги'})


def station_staff(reqest):
    posts = Amcarservice.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Наши сотрудники'
    }
    return render(reqest, 'Amcarservice/station_staff.html', context=context)


def pageNoteFound(reqest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def add_page(reqest):
    return HttpResponseNotFound('<h1>Добавление статьй</h1>')


def contact(reqest):
    return HttpResponseNotFound('<h1>Обратная связь</h1>')


def login(reqest):
    return HttpResponseNotFound('<h1>Авторизация</h1>')
