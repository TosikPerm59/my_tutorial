from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=45)
    content = models.TextField(blank=True)
    parent_name = models.CharField(max_length=45, default=0)
    date_of_change = models.DateField(auto_now=True)
    status = models.CharField(max_length=45, default=0)
    childrens = models.CharField(max_length=45, default=0)

    def __str__(self):
        return self.name

    # def defining_childrens(self):
    #     for article_ in Article.objects.all():
    #         if article_.parent_name == self.name:
    #             return article_.name
