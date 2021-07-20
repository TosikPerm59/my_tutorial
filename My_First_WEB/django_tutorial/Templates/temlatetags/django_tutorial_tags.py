from django import template
from django_tutorial.models import *


register = template.Library()


@register.simple_tag()
def get_articles():
    return Article.objects.all()


@register.simple_tag()
def links_list(element_id):
    link = str()
    links_l = []
    for example in get_articles():
        if example.id == element_id:
            links_l = example.links.split(';')
            return links_l

