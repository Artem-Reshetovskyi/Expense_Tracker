from django.shortcuts import render
from .models import Expense


def expense_list(request):
    category = request.GET.get("category")  # Отримуємо категорію з параметрів URL
    sort_by = request.GET.get("sort_by")  # Отримуємо параметр для сортування
    expenses = Expense.objects.all()  # За замовчуванням беремо всі витрати

    if category:
        expenses = expenses.filter(category=category)  # Фільтруємо за категорією, якщо вона передана
    if sort_by:
        if sort_by == 'amount':
            expenses = expenses.order_by('amount')  # Сортуємо за сумою
        elif sort_by == 'date':
            expenses = expenses.order_by('date')  # Сортуємо за датою

    return render(request, "expenses/expense_list.html", {"expenses": expenses})
