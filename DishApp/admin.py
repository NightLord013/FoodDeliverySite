from django.contrib import admin
from . import models

@admin.register(models.Category)
class AdminCategory(admin.ModelAdmin):
	list_display = ('name', 'is_available',)
	list_filter = ('name', 'is_available',)


class GalleryInline(admin.TabularInline):
	fk_name = 'dish'
	model = models.Gallery


@admin.register(models.Dish)
class AdminDish(admin.ModelAdmin):
	list_display = ('category', 'name', 'recipe', 'price', 'articul', 'description', 'is_available')
	list_filter = ('category', 'is_available')
	search_fields = ('name__startswith',)
	inlines = [GalleryInline,]
