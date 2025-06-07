"""
Views module for managing expenses.

This module contains functions to display a list of expenses,
add, edit, and delete expenses with authorization protection.
"""

from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ExpenseForm
from .models import Expense


@login_required
def expense_list(request):
    """
    Display a list of user's expenses with filtering and sorting options.

    Args:
        request (HttpRequest): The HTTP request from the user.

    Returns:
        HttpResponse: Rendered page with filtered and sorted expenses list.
    """
    expenses = Expense.objects.filter(user=request.user)
    category = request.GET.get("category")
    sort_by = request.GET.get("sort_by")

    if category:
        expenses = expenses.filter(category=category)

    date_from = request.GET.get("date_from", "")
    date_to = request.GET.get("date_to", "")
    if date_from:
        expenses = expenses.filter(date__gte=datetime.strptime(date_from, "%Y-%m-%d"))
    if date_to:
        expenses = expenses.filter(date__lte=datetime.strptime(date_to, "%Y-%m-%d"))

    if sort_by == "amount":
        expenses = expenses.order_by("amount")
    elif sort_by == "date":
        expenses = expenses.order_by("date")

    return render(request, "expenses/expense_list.html", {"expenses": expenses})


@login_required
def add_expense(request):
    """
    Handle the form to add a new expense.

    Args:
        request (HttpRequest): HTTP GET or POST request.

    Returns:
        HttpResponse: Redirect to expenses list on success or
                      page with form to add expense.
    """
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect("expenses:expense_list")
    else:
        form = ExpenseForm()

    return render(request, "expenses/add_expense.html", {"form": form})


@login_required
def edit_expense(request, pk):
    """
    Handle editing of an existing expense.

    Args:
        request (HttpRequest): HTTP GET or POST request.
        pk (int): ID of the expense to edit.

    Returns:
        HttpResponse: Redirect to expenses list on success or
                      page with edit form.
    """
    expense = get_object_or_404(Expense, id=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("expenses:expense_list")
    else:
        form = ExpenseForm(instance=expense)
    return render(
        request, "expenses/edit_expense.html", {"form": form, "expense": expense}
    )


@login_required
def delete_expense(request, pk):
    """
    Handle deletion of a specific expense.

    Args:
        request (HttpRequest): HTTP GET or POST request.
        pk (int): ID of the expense to delete.

    Returns:
        HttpResponse: Redirect to expenses list after deletion or
                      confirmation page.
    """
    expense = get_object_or_404(Expense, id=pk)
    if request.method == "POST":
        expense.delete()
        return redirect("expenses:expense_list")

    return render(request, "expenses/delete_expense.html", {"expense": expense})


@login_required
def delete_all_expenses(request):
    """
    Handle deletion of all expenses for the user.

    Args:
        request (HttpRequest): HTTP GET or POST request.

    Returns:
        HttpResponse: Redirect to expenses list after deletion or
                      confirmation page.
    """
    if request.method == "POST":
        Expense.objects.all().delete()
        return redirect("expenses:expense_list")

    return render(request, "expenses/delete_all_expenses.html")
