# Generated by Django 3.2.4 on 2021-06-28 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='images',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
