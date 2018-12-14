from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def select_group(request):
    return render(request, 'meal_managements/group/select_group.html', {'title': 'Meal Manager'})


@login_required
def create_group(request):
    return render(request, 'meal_managements/group/create_group.html', {'title': 'Create Group'})


@login_required
def join_group(request):
    return render(request, 'meal_managements/group/join_group.html', {'title': 'Join Group'})


@login_required
def dashboard(request):
    return render(request, 'meal_managements/dashboard.html', {'title': 'Dashboard'})
