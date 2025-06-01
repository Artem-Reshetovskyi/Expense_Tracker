from django.shortcuts import render
from django.db import models
from expenses.models import Expense
from incomes.models import Income
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime


def dashboard(request):
    today = timezone.now()
    start_date = datetime(today.year, today.month, 1)
    end_date = timezone.now()

    # Загальна сума доходів і витрат
    total_incomes = Income.objects.aggregate(total=models.Sum("amount"))["total"] or 0
    total_expenses = Expense.objects.aggregate(total=models.Sum("amount"))["total"] or 0

    
    # total_incomes = (
    #     Income.objects.filter(date__range=[start_date, end_date]).aggregate(
    #         total=models.Sum("amount")
    #     )["total"]
    #     or 0
    # )
    # total_expenses = (
    #     Expense.objects.filter(date__range=[start_date, end_date]).aggregate(
    #         total=models.Sum("amount")
    #     )["total"]
    #     or 0
    # )

    # Баланс
    balance = total_incomes - total_expenses

    context = {
        "total_expenses": total_expenses,
        "total_incomes": total_incomes,
        "balance": balance,
    }
    return render(request, "dashboard.html", context)
