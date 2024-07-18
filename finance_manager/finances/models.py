from django.db import models
from django.conf import settings
from django.utils import timezone

#Модель записи Дохода
class Income(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    comment = models.CharField(max_length = 100)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2, default=0)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.user} - {self.comment} - {self.amount}"

#Модель записи Расхода
class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    category = models.CharField(max_length = 100)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2, default=0)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.user} - {self.category} - {self.amount}"

#Модель записи Бюджета
class Budget(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    category = models.CharField(max_length = 100)
    limit =  models.DecimalField(max_digits=10, decimal_places=2, default=0)
    spent =  models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.user} - {self.category} - {self.limit} - {self.spent}"

#Модель записи Цели
class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    target_amount = models.DecimalField(max_digits = 10, decimal_places = 2, default=0)
    current_amount = models.DecimalField(max_digits = 10, decimal_places = 2, default=0)
    deadline = models.DateField()
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.user} - {self.name} - {self.target_amount} - {self.current_amount}"

