from audioop import reverse

from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=45, verbose_name='Название статьи')
    links = models.TextField(blank=True, null=True, verbose_name='Ссылки')
    content = models.TextField(blank=True)
    parent_name = models.CharField(max_length=45, default=0, verbose_name='Родительская статья')
    date_of_change = models.DateField(auto_now=True, verbose_name='Последнее редактирование')
    status = models.CharField(max_length=45, default=0)
    childrens = models.CharField(max_length=45, default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'
        ordering = ['-date_of_change', '-id']