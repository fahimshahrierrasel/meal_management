from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from users.models import Group, Membership


class MealType(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    count = models.SmallIntegerField()

    def __str__(self):
        return f'MealType({self.group}, {self.name}, {self.count})'


class Meal(models.Model):
    membership = models.ForeignKey(Membership, null=True, on_delete=models.SET_NULL)
    meal_type = models.ForeignKey(MealType, null=True, on_delete=models.SET_NULL)
    total = models.SmallIntegerField()
    mealed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Meal({self.membership}, {self.meal_type}, {self.total}, {self.mealed_at})'


class Shopping(models.Model):
    membership = models.ForeignKey(Membership, null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    shopped_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Shopping({self.membership}, {self.amount}, {self.shopped_at})'


class ShoppingItem(models.Model):
    shopping = models.ForeignKey(Shopping, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.SmallIntegerField()

    def __str__(self):
        return f'ShoppingItem({self.shopping}, {self.name}, {self.unit_price}, {self.quantity})'


class Voucher(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    vouched_at = models.DateField()

    def __str__(self):
        return f'Voucher({self.group}, {self.title}, {self.description}, {self.amount}, {self.vouched_at})'
