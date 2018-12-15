from users.models import Member, Membership


def user_membership_group(request):
    user = request.user
    member = Member.objects.filter(user=user).first()
    membership = Membership.objects.filter(member=member).first()
    group = membership.group
    data = {
        'current_member': member,
        'current_membership': membership,
        'current_group': group
    }

    return data
