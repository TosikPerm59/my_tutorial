# Generated by Django 3.2.4 on 2021-07-13 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_tutorial', '0011_article_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='links',
            field=models.TextField(blank=True, null=True),
        ),
    ]
