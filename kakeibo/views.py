from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Income, Expense
from .forms import IncomeForm, ExpenseForm
import calendar
from datetime import date, datetime

def add_income(request):
    year = int(request.GET.get('year', datetime.now().year))
    month = int(request.GET.get('month', datetime.now().month))
    
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_income')
    else:
        form = IncomeForm()
    
    incomes = Income.objects.filter(date__year=year, date__month=month)
    total_income = incomes.aggregate(Sum('amount'))['amount__sum'] or 0
    
    years = range(datetime.now().year - 10, datetime.now().year + 1)
    months = range(1, 13)
    
    context = {
        'form': form,
        'incomes': incomes,
        'total_income': total_income,
        'year': year,
        'month': month,
        'month_name': calendar.month_name[month],
        'years': years,
        'months': months,
    }
    return render(request, 'kakeibo/add_income.html', context)

def add_expense(request):
    year = int(request.GET.get('year', datetime.now().year))
    month = int(request.GET.get('month', datetime.now().month))
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_expense')
    else:
        form = ExpenseForm()
    
    expenses = Expense.objects.filter(date__year=year, date__month=month)
    total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    
    years = range(datetime.now().year - 10, datetime.now().year + 1)
    months = range(1, 13)
    
    context = {
        'form': form,
        'expenses': expenses,
        'total_expense': total_expense,
        'year': year,
        'month': month,
        'month_name': calendar.month_name[month],
        'years': years,
        'months': months,
    }
    return render(request, 'kakeibo/add_expense.html', context)

def delete_income(request, income_id):
    income = Income.objects.get(id=income_id)
    income.delete()
    return redirect('add_income')

def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    expense.delete()
    return redirect('add_expense')

def index(request):
    year = int(request.GET.get('year', datetime.now().year))
    month = int(request.GET.get('month', datetime.now().month))
    
    incomes = Income.objects.filter(date__year=year, date__month=month)
    expenses = Expense.objects.filter(date__year=year, date__month=month)
    
    total_income = incomes.aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    net_total = total_income - total_expense
    
    years = range(datetime.now().year - 10, datetime.now().year + 1)
    months = range(1, 13)
    
    context = {
        'incomes': incomes,
        'expenses': expenses,
        'total_income': total_income,
        'total_expense': total_expense,
        'net_total': net_total,
        'year': year,
        'month': month,
        'months': months,
        'years': years
    }
    return render(request, 'kakeibo/index.html', context)

def stats_view(request):
    # デフォルトの年と月
    year = int(request.GET.get('year', datetime.now().year))
    month = int(request.GET.get('month', datetime.now().month))

    # カテゴリ別収入と支出
    income_categories = Income.objects.filter(date__year=year, date__month=month) \
        .values('category') \
        .annotate(total=Sum('amount')) \
        .order_by()
    
    expense_categories = Expense.objects.filter(date__year=year, date__month=month) \
        .values('category') \
        .annotate(total=Sum('amount')) \
        .order_by()

    # 月別、年別の収支
    monthly_incomes = Income.objects.filter(date__year=year) \
        .values('date__month') \
        .annotate(total=Sum('amount')) \
        .order_by('date__month')
    
    yearly_incomes = Income.objects.all() \
        .values('date__year') \
        .annotate(total=Sum('amount')) \
        .order_by('date__year')
    
    monthly_expenses = Expense.objects.filter(date__year=year) \
        .values('date__month') \
        .annotate(total=Sum('amount')) \
        .order_by('date__month')
    
    yearly_expenses = Expense.objects.all() \
        .values('date__year') \
        .annotate(total=Sum('amount')) \
        .order_by('date__year')

    context = {
        'income_categories': income_categories,
        'expense_categories': expense_categories,
        'monthly_incomes': monthly_incomes,
        'yearly_incomes': yearly_incomes,
        'monthly_expenses': monthly_expenses,
        'yearly_expenses': yearly_expenses,
        'year': year,
        'month': month,
    }
    
    return render(request, 'kakeibo/stats_view.html', context)