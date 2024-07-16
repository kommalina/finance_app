from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Income, Expense, Budget, Goal
from .forms import IncomeForm, ExpenseForm, BudgetForm, GoalForm
from django.views.generic import UpdateView, DeleteView

def finance_home(request):
    return render(request, 'finances/finance_home.html')

class IncomeUpdateView(UpdateView):
    model = Income
    template_name = 'finances/income_create.html'
    form_class = IncomeForm
    success_url = reverse_lazy('income_list')

class IncomeDeleteView(DeleteView):
    model = Income
    template_name = 'finances/income_delete.html'
    success_url = reverse_lazy('income_list')


def income_create(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('finance_home')
    else:
        form = IncomeForm()
    return render(request, 'finances/income_create.html', {'form': form})
@login_required
def income_list(request):
    incomes = Income.objects.filter(user=request.user)
    return render(request, 'finances/income_list.html', {'incomes': incomes})

class ExpenseUpdateView(UpdateView):
    model = Expense
    template_name = 'finances/expense_create.html'
    form_class = ExpenseForm
    success_url = reverse_lazy('expense_list')

class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = 'finances/expense_delete.html'
    success_url = reverse_lazy('expense_list')

def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('finance_home')
    else:
        form = ExpenseForm()
    return render(request, 'finances/expense_create.html', {'form': form})
@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'finances/expense_list.html', {'expenses':expenses})

class BudgetUpdateView(UpdateView):
    model = Budget
    template_name = 'finances/budget_create.html'
    form_class = BudgetForm
    success_url = reverse_lazy('budget_list')

class BudgetDeleteView(DeleteView):
    model = Budget
    template_name = 'finances/budget_delete.html'
    success_url = reverse_lazy('budget_list')

def budget_create(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('finance_home')
    else:
        form = BudgetForm()
    return render(request, 'finances/budget_create.html', {'form': form})
@login_required
def budget_list(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'finances/budget_list.html', {'budgets':budgets})

class GoalUpdateView(UpdateView):
    model = Goal
    template_name = 'finances/goal_create.html'
    form_class = GoalForm
    success_url = reverse_lazy('goal_list')

class GoalDeleteView(DeleteView):
    model = Goal
    template_name = 'finances/goal_delete.html'
    success_url = reverse_lazy('goal_list')

def goal_create(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('finance_home')
    else:
        form = GoalForm()
    return render(request, 'finances/goal_create.html', {'form': form})
@login_required
def goal_list(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'finances/goal_list.html', {'goals':goals})