import uuid as uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Member(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=12)
    address = models.TextField()
    emergency_contact_number = models.CharField(max_length=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Member({self.name}, {self.mobile_number}, \
            {self.address}, {self.emergency_contact_number})'


class Group(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    address = models.TextField()
    captain = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'Group({self.name}, {self.address}, {self.captain})'


class Membership(models.Model):
    member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Membership({self.group}, {self.member}, {self.status}, {self.date_joined})'
