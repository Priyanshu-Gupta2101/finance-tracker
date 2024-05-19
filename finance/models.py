# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Income(models.Model):
    source = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return { self.source, self.user, self.date, self.amount, self.description} 

class Expense(models.Model):
    category = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return {self.category, self.user, self.date, self.amount, self.description} 
