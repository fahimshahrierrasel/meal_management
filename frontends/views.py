from django.shortcuts import render


def home(request):
    return render(request, 'meal_management/index.html', {'title': 'Meal Manager'})


def new_meal_group(request):
    return render(request, 'meal_management/new_meal_group.html', {'title': 'New Meal Group'})
