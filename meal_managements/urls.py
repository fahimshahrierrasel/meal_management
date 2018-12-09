from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    # path('new-meal-group', views.new_meal_group, name='new-meal-group'),
]
