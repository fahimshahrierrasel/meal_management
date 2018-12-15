from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import MealType
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


@login_required
def group_members(request, slug):
    group = Group.objects.filter(uuid=slug).first()
    memberships = Membership.objects.filter(group=group).all()

    data = {
        'title': f"{group.name}'s Members",
        'memberships': memberships
    }
    return render(request, 'meal_managements/member/members.html', context=data)


@login_required
def group_info(request, slug):
    group = Group.objects.filter(uuid=slug).first()
    total_members = Membership.objects.filter(group=group).all().count()
    data = {
        'title': f"{group.name}'s Info",
        'group': group,
        'total_members': total_members
    }
    return render(request, 'meal_managements/group/group_info.html', context=data)


@login_required
def meal_types(request, slug):
    group = Group.objects.filter(uuid=slug).first()
    if request.POST:
        name = request.POST['name']
        count = request.POST['count']

        MealType.objects.create(
            name=name,
            count=count,
            group=group
        )

        return redirect('meal_types', slug=group.uuid)

    types = MealType.objects.filter(group=group).all()
    data = {
        'title': f"{group.name}'s Meal Types",
        'meal_types': types
    }
    return render(request, 'meal_managements/meal/meal_types.html', context=data)
