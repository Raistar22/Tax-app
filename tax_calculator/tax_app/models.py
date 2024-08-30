from django.contrib.auth.models import User
from django.db import models

class TaxSlab(models.Model):
    year = models.IntegerField()
    slab_type = models.CharField(max_length=10)  # 'old' or 'new'
    income_from = models.DecimalField(max_digits=10, decimal_places=2)
    income_to = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)

class Deduction(models.Model):
    type = models.CharField(max_length=100)
    max_amount = models.DecimalField(max_digits=10, decimal_places=2)

class TaxPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    deductions = models.JSONField(default=dict)  # Store deductions as a JSON object
    calculated_tax = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
