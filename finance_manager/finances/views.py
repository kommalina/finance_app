from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Income, Expense, Budget, Goal
from .forms import IncomeForm, ExpenseForm, BudgetForm, GoalForm
from django.views.generic import CreateView, UpdateView, DeleteView

#Отображение домашней страницы с финансами
def finance_home(request):
    return render(request, 'finances/finance_home.html')

#Класс Редактирования записи о доходах
class IncomeUpdateView(UpdateView):
    model = Income
    template_name = 'finances/income_create.html'
    form_class = IncomeForm
    success_url = reverse_lazy('income_list')

#Класс Удаления записи о доходах
class IncomeDeleteView(DeleteView):
    model = Income
    template_name = 'finances/income_delete.html'
    success_url = reverse_lazy('income_list')

#Класс Создания записи о доходах
class IncomeCreateView(CreateView):
    model = Income
    template_name = 'finances/income_create.html'
    form_class = IncomeForm
    success_url = reverse_lazy('income_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#Отображение всех записей доходов
@login_required
def income_list(request):
    incomes = Income.objects.filter(user=request.user)
    return render(request, 'finances/income_list.html', {'incomes': incomes})

#Класс Редактирования записи о расходах
class ExpenseUpdateView(UpdateView):
    model = Expense
    template_name = 'finances/expense_create.html'
    form_class = ExpenseForm
    success_url = reverse_lazy('expense_list')

#Класс Удаления записи о расходах
class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = 'finances/expense_delete.html'
    success_url = reverse_lazy('expense_list')

#Класс Создания записи о расходах
class ExpenseCreateView(CreateView):
    model = Expense
    template_name = 'finances/expense_create.html'
    form_class = ExpenseForm
    success_url = reverse_lazy('expense_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#Отображение всех записей расходов
@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'finances/expense_list.html', {'expenses':expenses})

#Класс Реадактирования записи о бюджетах
class BudgetUpdateView(UpdateView):
    model = Budget
    template_name = 'finances/budget_create.html'
    form_class = BudgetForm
    success_url = reverse_lazy('budget_list')

#Класс Удаления записи о бюджетах
class BudgetDeleteView(DeleteView):
    model = Budget
    template_name = 'finances/budget_delete.html'
    success_url = reverse_lazy('budget_list')

#Класс Создания записи о бюджетах
class BudgetCreateView(CreateView):
    model = Budget
    template_name = 'finances/budget_delete.html'
    success_url = reverse_lazy('budget_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#Отображение всех записей бюджетов
@login_required
def budget_list(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'finances/budget_list.html', {'budgets':budgets})

#Класс Реадиктирования записи о целях
class GoalUpdateView(UpdateView):
    model = Goal
    template_name = 'finances/goal_create.html'
    form_class = GoalForm
    success_url = reverse_lazy('goal_list')

#Класс Удаления записи о целях
class GoalDeleteView(DeleteView):
    model = Goal
    template_name = 'finances/goal_delete.html'
    success_url = reverse_lazy('goal_list')

#Класс Создания записи о целях
class GoalCreateView(CreateView):
    model = Goal
    template_name = 'finances/goal_delete.html'
    success_url = reverse_lazy('goal_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#Отображение всех записей целей
@login_required
def goal_list(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'finances/goal_list.html', {'goals':goals})