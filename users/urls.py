from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register', views.register, name='register'),

    path('login', auth_views.LoginView.as_view(
        template_name='users/login.html',
        extra_context={'title': 'Login'}), name='login'),

    path('logout', auth_views.LogoutView.as_view(
        template_name='users/logout.html',
        extra_context={'title': 'Logout'}), name='logout'),

    path('new-member', views.new_member, name='new_member'),

    path('<slug:slug>/profile', views.profile, name='profile'),
]
