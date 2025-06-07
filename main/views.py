from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from expenses.models import Expense
from incomes.models import Income
from django.utils.translation import gettext as _
import json


@login_required
def dashboard(request):
    """
    Render the dashboard page showing total incomes, expenses, balance,
    and chart data filtered optionally by date range.

    Args:
        request (HttpRequest): The HTTP request object, may contain GET parameters
                               "start_date" and "end_date" for filtering data.

    Returns:
        HttpResponse: Rendered dashboard page with context data including:
                      - total incomes and expenses,
                      - balance,
                      - JSON-encoded data for charts of expenses by category
                        and incomes by description.
    """
    # Get start and end dates from GET parameters
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

    # Chart data: expenses by category
    expenses_by_category = expense_queryset.values("category").annotate(
        total=Sum("amount")
    )
    category_labels = [
        str(Expense.CategoryChoices(item["category"]).label) for item in expenses_by_category
    ]
    category_data = [round(float(item["total"]), 2) for item in expenses_by_category]

    # Chart data: incomes by description
    incomes_by_description = income_queryset.values("description").annotate(
        total=Sum("amount")
    )
    income_labels = [
        str(Income.DescriptionChoices(item["description"]).label) for item in incomes_by_description
    ]
    income_data = [round(float(item["total"]), 2) for item in incomes_by_description]

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
