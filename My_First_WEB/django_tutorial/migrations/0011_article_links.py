# Generated by Django 3.2.4 on 2021-07-13 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_tutorial', '0010_auto_20210708_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='links',
            field=models.TextField(null=True),
        ),
    ]