# Generated by Django 3.2.5 on 2021-09-21 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('is_available', models.BooleanField(default=True, verbose_name='Доступен')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категрии',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Название')),
                ('recipe', models.CharField(max_length=200, verbose_name='Рецепт')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('articul', models.IntegerField(verbose_name='Артикуль')),
                ('description', models.TextField(verbose_name='Описание')),
                ('is_available', models.BooleanField(default=True, verbose_name='Доступен')),
                ('caletory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='DishApp.category', verbose_name='Категрия')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='galery', verbose_name='Фото')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='DishApp.dish')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]