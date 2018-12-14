from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.models import Membership, Member, Group


@login_required
def select_group(request):
    return render(request, 'meal_managements/group/select_group.html', {'title': 'Meal Manager'})


@login_required
def create_group(request):
    if request.POST:
        member = Member.objects.filter(user=request.user).first()
        name = request.POST['name']
        address = request.POST['address']

        group = Group.objects.create(
            name=name,
            address=address,
            captain=member
        )

        Membership.objects.create(
            member=member,
            group=group,
            status=True
        )

        return redirect('dashboard')

    return render(request, 'meal_managements/group/create_group.html', {'title': 'Create Group'})


@login_required
def join_group(request):
    return render(request, 'meal_managements/group/join_group.html', {'title': 'Join Group'})


@login_required
def dashboard(request):
    user = request.user
    member = Member.objects.filter(user=user).first()
    membership = Membership.objects.filter(member=member).first()
    if not member:
        return redirect('new_member')
    elif not membership:
        return redirect('select_group')
    else:
        return render(request, 'meal_managements/dashboard.html', {'title': 'Dashboard'})
