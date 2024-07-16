from .models import Income, Expense, Budget, Goal
from django.forms import ModelForm

class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ['comment', 'amount']

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount']

class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'limit', 'spent']

class GoalForm(ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'target_amount', 'current_amount', 'deadline']