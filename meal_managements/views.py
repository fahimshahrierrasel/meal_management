from django.shortcuts import render


def dashboard(request):
    return render(request, 'meal_managements/dashboard.html')
