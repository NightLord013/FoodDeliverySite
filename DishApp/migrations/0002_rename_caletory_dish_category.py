# Generated by Django 3.2.5 on 2021-09-21 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DishApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='caletory',
            new_name='category',
        ),
    ]
