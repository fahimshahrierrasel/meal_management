from django.shortcuts import render


def select_group(request):
    return render(request, 'meal_managements/select_group.html', {'title': 'Meal Manager'})


def create_group(request):
    return render(request, 'meal_managements/group/create_group.html', {'title': 'Create Group'})


def dashboard(request):
    return render(request, 'meal_managements/dashboard.html', {'title': 'Dashboard'})
