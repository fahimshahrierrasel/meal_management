from django.urls import path
from . import views

urlpatterns = [
    path('select-group', views.select_group, name='select_group'),
    path('create-group', views.create_group, name='create_group'),
    path('join-group', views.join_group, name='join_group'),
    path('dashboard', views.dashboard, name='dashboard'),
]
