from django.shortcuts import render
from django.db import models
from django.contrib.auth.decorators import (
    login_required,
)
from expenses.models import Expense
from incomes.models import Income
from django.db.models import Sum
from django.utils import timezone
from django.utils.translation import gettext as _
from datetime import datetime
from collections import defaultdict
import json

@login_required
def dashboard(request):

    # Загальна сума доходів і витрат
    total_incomes = Income.objects.aggregate(total=models.Sum("amount"))["total"] or 0
    total_expenses = Expense.objects.aggregate(total=models.Sum("amount"))["total"] or 0

    # Баланс
    balance = total_incomes - total_expenses

    # Дані для діаграми витрат по категоріях
    expenses_by_category = (
        Expense.objects.filter(user=request.user)
        .values("category")
        .annotate(total=Sum("amount"))
    )
    category_labels = [_(item["category"]) for item in expenses_by_category]
    category_data = [float(item["total"]) for item in expenses_by_category]

    # Дані для діаграми доходів по описах
    incomes_by_description = (
        Income.objects.filter(user=request.user)
        .values("description")
        .annotate(total=Sum("amount"))
    )
    income_labels = [_(item["description"]) for item in incomes_by_description]
    income_data = [float(item["total"]) for item in incomes_by_description]

    context = {
        "total_expenses": total_expenses,
        "total_incomes": total_incomes,
        "balance": balance,
        "category_labels": json.dumps(category_labels),
        "category_data": json.dumps(category_data),
        "income_labels": json.dumps(income_labels),
        "income_data": json.dumps(income_data),
    }
    
    return render(request, "main/dashboard.html", context)
