from django.db import models

class Category(models.Model):
	
	name = models.CharField(max_length=50, verbose_name='Название')
	is_available = models.BooleanField(default=True, verbose_name='Доступен')

	class Meta:
		ordering = ('name',)
		verbose_name = 'Категория'
		verbose_name_plural = 'Категрии'

	def __str__(self):
		return self.name


class Dish(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes', verbose_name='Категрия')
	name = models.CharField(max_length=75, verbose_name='Название')
	recipe = models.CharField(max_length=200, verbose_name='Рецепт')
	price = models.IntegerField(verbose_name='Цена')
	articul = models.IntegerField(verbose_name='Артикуль')
	description = models.TextField(verbose_name='Описание')
	is_available = models.BooleanField(default=True, verbose_name='Доступен')

	class Meta:
		verbose_name = 'Блюдо'
		verbose_name_plural = 'Блюда'

	def __str__(self):
		return self.name


class Gallery(models.Model):
	image = models.ImageField(upload_to='gallery', verbose_name='Фото')
	dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='images')

	class Meta:
		verbose_name = 'Фотография'
		verbose_name_plural = 'Фотографии'


