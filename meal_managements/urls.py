from django.urls import path
from . import views

urlpatterns = [
    path('select-group', views.select_group, name='select_group'),
    path('create-group', views.create_group, name='create_group'),
    path('join-group', views.join_group, name='join_group'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('<slug:slug>/members', views.group_members, name='group_members'),
    path('<slug:slug>/info', views.group_info, name='group_info'),
    path('<slug:slug>/meal-types', views.meal_types, name='meal_types'),
]
