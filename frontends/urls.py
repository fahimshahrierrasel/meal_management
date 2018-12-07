from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new-meal-group', views.new_meal_group, name='new-meal-group'),
]