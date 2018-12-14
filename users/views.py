from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import UserModel

from .models import Member
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


@login_required
def new_member(request):
    # TODO Check user is already a member
    if request.POST:
        user = request.user
        name = request.POST['name']
        mobile_number = request.POST['mobile_number']
        address = request.POST['address']
        emergency_contact = request.POST['emergency_contact']

        Member.objects.create(
            name=name,
            mobile_number=mobile_number,
            address=address,
            emergency_contact_number=emergency_contact,
            user=user
        )

        return redirect('dashboard')

    return render(request, 'users/new_member.html', {'title': 'New Member Info'})


@login_required
def profile(request, slug):
    user = UserModel.objects.filter(username=slug).get()
    data = {
        'title': f"{slug}'s Profile",
        'user': user
    }
    return render(request, 'users/profile.html', context=data)
