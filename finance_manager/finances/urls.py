from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.finance_home,name = 'finance_home'),                                             #Home page
    path('income/', views.income_list, name = 'income_list'),                                       #Page with all income records
    path('income/create/', views.IncomeCreateView.as_view(), name = 'income_create'),               #Create an income record
    path('income/<int:pk>/update/', views.IncomeUpdateView.as_view(), name = 'income_update'),      #Update/edit an income record
    path('income/<int:pk>/delete/', views.IncomeDeleteView.as_view(), name = 'income_delete'),      #Delete income record
    path('expense/', views.expense_list, name = 'expense_list'),                                    #Page with all expense records
    path('expense/create/', views.ExpenseCreateView.as_view(), name = 'expense_create'),            #Create an expense record
    path('expense/<int:pk>/update/', views.ExpenseUpdateView.as_view(), name = 'expense_update'),   #Update/edit an expense record
    path('expense/<int:pk>/delete/', views.ExpenseDeleteView.as_view(), name = 'expense_delete'),   #Delete expense record
    path('budget/', views.budget_list, name = 'budget_list'),                                       #Page with list of budgets
    path('budget/create/', views.BudgetCreateView.as_view(), name = 'budget_create'),               #Create a budget record
    path('budget/<int:pk>/update/', views.BudgetUpdateView.as_view(), name = 'budget_update'),      #Update/edit a budget record
    path('budget/<int:pk>/delete/', views.BudgetDeleteView.as_view(), name = 'budget_delete'),      #Delete budget record
    path('goal/', views.goal_list, name = 'goal_list'),                                             #Page with all your goals
    path('goal/create', views.GoalCreateView.as_view(), name = 'goal_create'),                      #Create a goal
    path('goal/<int:pk>/update/', views.GoalUpdateView.as_view(), name = 'goal_update'),            #Update/edit a goal
    path('goal/<int:pk>/delete/', views.GoalDeleteView.as_view(), name = 'goal_delete'),            #Delete goal
]