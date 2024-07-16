from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.finance_home,name = 'finance_home'),
    path('income/', views.income_list, name = 'income_list'),
    path('income/create/', views.income_create, name = 'income_create'),
    path('income/<int:pk>/update/', views.IncomeUpdateView.as_view(), name = 'income_update'),
    path('income/<int:pk>/delete/', views.IncomeDeleteView.as_view(), name = 'income_delete'),
    path('expense/', views.expense_list, name = 'expense_list'),
    path('expense/create/', views.expense_create, name = 'expense_create'),
    path('expense/<int:pk>/update/', views.ExpenseUpdateView.as_view(), name = 'expense_update'),
    path('expense/<int:pk>/delete/', views.ExpenseDeleteView.as_view(), name = 'expense_delete'),
    path('budget/', views.budget_list, name = 'budget_list'),
    path('budget/create/', views.budget_create, name = 'budget_create'),
    path('budget/<int:pk>/update/', views.BudgetUpdateView.as_view(), name = 'budget_update'),
    path('budget/<int:pk>/delete/', views.BudgetDeleteView.as_view(), name = 'budget_delete'),
    path('goal/', views.goal_list, name = 'goal_list'),
    path('goal/create', views.goal_create, name = 'goal_create'),
    path('goal/<int:pk>/update/', views.GoalUpdateView.as_view(), name = 'goal_update'),
    path('goal/<int:pk>/delete/', views.GoalDeleteView.as_view(), name = 'goal_delete'),
]