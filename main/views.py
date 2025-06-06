from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from expenses.models import Expense
from incomes.models import Income
from django.utils.translation import gettext as _
import json


@login_required
def dashboard(request):
    # Отримання дати початку та кінця з GET параметрів
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    income_queryset = Income.objects.filter(user=request.user)
    expense_queryset = Expense.objects.filter(user=request.user)

    if start_date and end_date:
        income_queryset = income_queryset.filter(date__range=[start_date, end_date])
        expense_queryset = expense_queryset.filter(date__range=[start_date, end_date])

    total_incomes = income_queryset.aggregate(total=Sum("amount"))["total"] or 0
    total_expenses = expense_queryset.aggregate(total=Sum("amount"))["total"] or 0
    balance = total_incomes - total_expenses

    # Дані для діаграми витрат по категоріях
    expenses_by_category = expense_queryset.values("category").annotate(
        total=Sum("amount")
    )
    category_labels = [_(item["category"]) for item in expenses_by_category]
    category_data = [float(item["total"]) for item in expenses_by_category]

    # Дані для діаграми доходів по описах
    incomes_by_description = income_queryset.values("description").annotate(
        total=Sum("amount")
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
