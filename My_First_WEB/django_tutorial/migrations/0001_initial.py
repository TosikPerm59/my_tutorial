# Generated by Django 3.2.4 on 2021-06-28 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('parent_name', models.CharField(max_length=30)),
                ('date_of_change', models.DateField(auto_now=True)),
                ('images', models.ImageField(upload_to='')),
            ],
        ),
    ]
