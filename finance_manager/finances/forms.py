from .models import Income, Expense, Budget, Goal
from django.forms import ModelForm

#Форма записи Дохода
class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ['comment', 'amount']

#Форма записи Расхода
class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount']

#Форма записи Бюджета
class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'limit', 'spent']

#Форма записи Цели
class GoalForm(ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'target_amount', 'current_amount', 'deadline']