from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.report_home, name = 'report_home'),                      #To homepage
    path('income_report', views.income_report, name = 'income_report'),     #View income report
    path('expense_report', views.expense_report, name = 'expense_report')   #View expense report
]

