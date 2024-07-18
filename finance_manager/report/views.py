import pandas as pd
import plotly.express as px
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from finances.models import Income, Expense

#Главная страница отчета
def report_home(request):
    return render(request, 'report/report_home.html')

#Гистограмма доходов
@login_required
def income_report(request):
    incomes = Income.objects.filter(user=request.user).values('amount', 'date')

    df = pd.DataFrame(incomes)

    #Извлечение месяца и года из date
    df['month_year'] = df['date'].dt.to_period('M')

    #Группирование по месяцам и суммирование
    monthly_income = df.groupby('month_year')['amount'].sum().reset_index()

    #Для сериализации в JSON
    monthly_income['month_year'] = monthly_income['month_year'].astype(str)

    #Построение гистограммы
    fig = px.bar(monthly_income, x='month_year', y='amount',
                 labels={'month_year': 'Месяц', 'amount': 'Сумма доходов'})

    fig.update_layout(
        title='Сумма доходов по месяцам',
        xaxis_title='Месяц',
        yaxis_title='Сумма доходов',
    )
    config = {
        'displayModeBar': False
    }

    graph_html = fig.to_html(full_html=False, default_height=500, default_width=700, config=config)

    return render(request, 'report/income_report.html', {'graph_html': graph_html})

#Гистограмма расходов
@login_required
def expense_report(request):
    expenses = Expense.objects.filter(user=request.user).values('amount', 'date')

    df = pd.DataFrame(expenses)

    # Извлечение месяца и года из date
    df['month_year'] = df['date'].dt.to_period('M')

    # Группирование по месяцам и суммирование
    month_expense = df.groupby('month_year')['amount'].sum().reset_index()

    # Для сериализации в JSON
    month_expense['month_year'] = month_expense['month_year'].astype(str)

    # Построение гистограммы
    fig = px.bar(month_expense, x='month_year', y='amount',
                 labels={'month_year': 'Месяц', 'amount': 'Сумма доходов'})

    fig.update_layout(
        title='Сумма расходов по месяцам',
        xaxis_title='Месяц',
        yaxis_title='Сумма расходов',
    )

    config = {
        'displayModeBar': False
    }

    graph_html = fig.to_html(full_html=False, default_height=500, default_width=700, config = config)

    return render(request, 'report/expense_report.html', {'graph_html': graph_html})
