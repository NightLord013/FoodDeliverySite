from django.shortcuts import render
from .models import Dish
from django.views.generic.list import ListView

class Home(ListView):
	model = Dish
	template_name = 'DishApp/home.html'
	context_object_name = 'dishes'
