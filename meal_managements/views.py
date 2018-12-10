from django.shortcuts import render


def select_group(request):
    return render(request, 'meal_managements/select_group.html', {'title': 'Meal Manager'})


def dashboard(request):
    return render(request, 'meal_managements/dashboard.html', {'title': 'Dashboard'})
