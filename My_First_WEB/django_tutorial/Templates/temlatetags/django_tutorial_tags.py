from django import template
from django_tutorial.models import *


register = template.Library()


@register.simple_tag()
def get_articles():
    return Article.objects.all()
