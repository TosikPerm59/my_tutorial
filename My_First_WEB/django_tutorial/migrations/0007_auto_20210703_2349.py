# Generated by Django 3.2.4 on 2021-07-03 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_tutorial', '0006_alter_article_parent_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='childrens',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='article',
            name='parent_name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
