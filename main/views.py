from django.shortcuts import render
from django.db.models import Sum
from expenses.models import Expense
from incomes.models import Income  # Якщо доходи в окремому додатку incomes


def dashboard(request):
    total_expenses = Expense.objects.aggregate(total=Sum("amount"))["total"] or 0
    total_incomes = Income.objects.aggregate(total=Sum("amount"))["total"] or 0
    balance = total_incomes - total_expenses

    context = {
        "total_expenses": total_expenses,
        "total_incomes": total_incomes,
        "balance": balance,
    }
    return render(request, "dashboard.html", context)
