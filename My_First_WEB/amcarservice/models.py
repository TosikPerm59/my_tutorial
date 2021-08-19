from django.db import models


class Amcarservice(models.Model):
    name = models.CharField(max_length=30)
    sur_name = models.CharField(max_length=30)
    age = models.CharField(max_length=2)
    position = models.CharField(max_length=130)
    photo = models.ImageField(upload_to='')






