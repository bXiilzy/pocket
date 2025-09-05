from django.db import models
from django.contrib.auth.models import User
from datetime import date as Date

# Create your models here.

# part 3
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # details
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # money
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.IntegerField(choices=[(1, "Income"), (-1, "Expense")])
    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
