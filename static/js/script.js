document.addEventListener('DOMContentLoaded', function() {
    const incomeCategoriesCtx = document.getElementById('incomeCategoriesChart').getContext('2d');
    const expenseCategoriesCtx = document.getElementById('expenseCategoriesChart').getContext('2d');
    const monthlyIncomesCtx = document.getElementById('monthlyIncomesChart').getContext('2d');
    const yearlyIncomesCtx = document.getElementById('yearlyIncomesChart').getContext('2d');
    const monthlyExpensesCtx = document.getElementById('monthlyExpensesChart').getContext('2d');
    const yearlyExpensesCtx = document.getElementById('yearlyExpensesChart').getContext('2d');

    const incomeCategoriesData = {
        labels: [{% for category in income_categories %}"{{ category.category }}"{% if not forloop.last %},{% endif %}{% endfor %}],
        datasets: [{
            data: [{% for category in income_categories %}{{ category.total }}{% if not forloop.last %},{% endif %}{% endfor %}],
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56']
        }]
    };

    const expenseCategoriesData = {
        labels: [{% for category in expense_categories %}"{{ category.category }}"{% if not forloop.last %},{% endif %}{% endfor %}],
        datasets: [{
            data: [{% for category in expense_categories %}{{ category.total }}{% if not forloop.last %},{% endif %}{% endfor %}],
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56']
        }]
    };

    const monthlyIncomesData = {
        labels: [{% for m in monthly_incomes %}"{{ m.date__month }}"{% if not forloop.last %},{% endif %}{% endfor %}],
        datasets: [{
            label: '収入',
            data: [{% for income in monthly_incomes %}{{ income.total }}{% if not forloop.last %},{% endif %}{% endfor %}],
            backgroundColor: '#36A2EB'
        }]
    };

    const yearlyIncomesData = {
        labels: [{% for y in yearly_incomes %}"{{ y.date__year }}"{% if not forloop.last %},{% endif %}{% endfor %}],
        datasets: [{
            label: '収入',
            data: [{% for income in yearly_incomes %}{{ income.total }}{% if not forloop.last %},{% endif %}{% endfor %}],
            backgroundColor: '#36A2EB'
        }]
    };

    const monthlyExpensesData = {
        labels: [{% for m in monthly_expenses %}"{{ m.date__month }}"{% if not forloop.last %},{% endif %}{% endfor %}],
        datasets: [{
            label: '支出',
            data: [{% for expense in monthly_expenses %}{{ expense.total }}{% if not forloop.last %},{% endif %}{% endfor %}],
            backgroundColor: '#FF6384'
        }]
    };

    const yearlyExpensesData = {
        labels: [{% for y in yearly_expenses %}"{{ y.date__year }}"{% if not forloop.last %},{% endif %}{% endfor %}],
        datasets: [{
            label: '支出',
            data: [{% for expense in yearly_expenses %}{{ expense.total }}{% if not forloop.last %},{% endif %}{% endfor %}],
            backgroundColor: '#FF6384'
        }]
    };

    new Chart(incomeCategoriesCtx, {
        type: 'pie',
        data: incomeCategoriesData,
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });

    new Chart(expenseCategoriesCtx, {
        type: 'pie',
        data: expenseCategoriesData
    });

    new Chart(monthlyIncomesCtx, {
        type: 'bar',
        data: monthlyIncomesData
    });

    new Chart(yearlyIncomesCtx, {
        type: 'bar',
        data: yearlyIncomesData
    });

    new Chart(monthlyExpensesCtx, {
        type: 'bar',
        data: monthlyExpensesData
    });

    new Chart(yearlyExpensesCtx, {
        type: 'bar',
        data: yearlyExpensesData
    });
});
