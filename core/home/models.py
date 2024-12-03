from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Expense(models.Model):
    RECORD_TYPE_CHOICES = [
        ('expense', 'Расход'),
        ('income', 'Доход'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    date = models.DateField(default=datetime.now)
    record_type = models.CharField(
        max_length=7,
        choices=RECORD_TYPE_CHOICES,
        default='expense',
    )

    class Meta:
        ordering = ["-date"]