# Generated by Django 4.1.3 on 2022-12-13 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adminpanel', '0004_visiteur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visiteur',
            name='residence',
        ),
        migrations.RemoveField(
            model_name='visiteur',
            name='sexe',
        ),
    ]
