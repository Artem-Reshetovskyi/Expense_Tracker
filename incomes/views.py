from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import now

from .forms import IncomeForm
from .models import Income


@login_required
def income_list(request):
    """
    Display a list of user incomes with optional filtering and sorting.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered page displaying filtered and sorted incomes.
    """
    incomes = Income.objects.filter(user=request.user)

    description = request.GET.get("description")
    if description:
        incomes = incomes.filter(description=description)

    date_from = request.GET.get("date_from", "")
    date_to = request.GET.get("date_to", "")
    if date_from:
        incomes = incomes.filter(date__gte=datetime.strptime(date_from, "%Y-%m-%d"))
    if date_to:
        incomes = incomes.filter(date__lte=datetime.strptime(date_to, "%Y-%m-%d"))

    sort_by = request.GET.get("sort_by", "")
    if sort_by == "amount":
        incomes = incomes.order_by("amount")
    elif sort_by == "date":
        incomes = incomes.order_by("date")

    return render(request, "incomes/income_list.html", {"incomes": incomes})


@login_required
def add_income(request):
    """
    Handle the form for adding a new income entry.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirect to income list if successful or
                      render the form page otherwise.
    """
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect("incomes:income_list")
    else:
        form = IncomeForm()
    return render(request, "incomes/income_form.html", {"form": form})


@login_required
def income_edit(request, pk):
    """
    Handle editing an existing income entry.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): Primary key of the income to edit.

    Returns:
        HttpResponse: Redirect to income list if successful or
                      render the form page otherwise.
    """
    income = get_object_or_404(Income, pk=pk, user=request.user)
    if request.method == "POST":
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect("incomes:income_list")
    else:
        form = IncomeForm(instance=income)
    return render(request, "incomes/income_form.html", {"form": form})


@login_required
def income_delete(request, pk):
    """
    Handle deletion of a specific income entry.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): Primary key of the income to delete.

    Returns:
        HttpResponse: Redirect to income list after deletion or
                      render the confirmation page.
    """
    income = get_object_or_404(Income, pk=pk, user=request.user)
    if request.method == "POST":
        income.delete()
        return redirect("incomes:income_list")
    return render(request, "incomes/income_confirm_delete.html", {"income": income})


@login_required
def delete_all_incomes(request):
    """
    Handle deletion of all incomes for the current user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirect to income list after deletion or
                      render the confirmation page.
    """
    if request.method == "POST":
        Income.objects.filter(user=request.user).delete()
        return redirect("incomes:income_list")
    return render(request, "incomes/delete_all_incomes.html")
