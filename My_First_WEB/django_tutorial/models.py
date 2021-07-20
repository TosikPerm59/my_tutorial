from audioop import reverse

from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=45)
    links = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True)
    parent_name = models.CharField(max_length=45, default=0)
    date_of_change = models.DateField(auto_now=True)
    status = models.CharField(max_length=45, default=0)
    childrens = models.CharField(max_length=45, default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article', kwargs={'article_id': self.id})
