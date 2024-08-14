def history_view(request):
    year = request.GET.get('year', datetime.now().year)
    month = request.GET.get('month', datetime.now().month)
    
    incomes = Income.objects.filter(date__year=year, date__month=month)
    expenses = Expense.objects.filter(date__year=year, date__month=month)
    
    print(f"Year: {year}, Month: {month}")
    print(f"Incomes: {incomes}")
    print(f"Expenses: {expenses}")
    
    total_income = incomes.aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    net_total = total_income - total_expense
    
    context = {
        'incomes': incomes,
        'expenses': expenses,
        'total_income': total_income,
        'total_expense': total_expense,
        'net_total': net_total,
        'year': year,
        'month': month,
        'month_name': calendar.month_name[int(month)]
    }
    return render(request, 'kakeibo/history_view.html', context)