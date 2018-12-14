from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import UserModel
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} your account created!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'title': 'Register', 'form': form})


def profile(request, slug):
    user = UserModel.objects.filter(username=slug).get()
    data = {
        'title': f"{slug}'s Profile",
        'user': user
    }
    return render(request, 'users/profile.html', context=data)
