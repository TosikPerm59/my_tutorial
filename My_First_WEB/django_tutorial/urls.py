from django.urls import path

from django_tutorial.views import *

urlpatterns = [
    path('', index_djtut, name='djtut'),
    path('article/<int:article_id>/', show_article, name='article'),
    path('search_request/', search_results, name='search_results'),

]