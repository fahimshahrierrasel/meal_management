from django.shortcuts import render


def home(request):
    return render(request, 'frontends/index.html', {'title': 'Meal Manager'})


def new_meal_group(request):
    return render(request, 'frontends/new_meal_group.html', {'title': 'New Meal Group'})
