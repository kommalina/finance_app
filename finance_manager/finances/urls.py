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
    path('budget/', views.budget_list, name = 'budget_list'),
    path('budget/create/', views.budget_create, name = 'budget_create'),
    path('goal/', views.goal_list, name = 'goal_list'),
    path('goal/create', views.goal_create, name = 'goal_create')
]