# Generated by Django 3.2.4 on 2021-07-03 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_tutorial', '0004_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='childrens',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
