from django.shortcuts import render, redirect, get_object_or_404
from .models import Income
from .forms import IncomeForm
from django.db.models import Q
from datetime import datetime
from django.db.models import Sum
from django.utils.timezone import now
from datetime import timedelta
from django.contrib.auth.decorators import login_required # Декоратор для захисту від неавторизованого доступу  

# Incomes - це доходи користувача, які він може додавати, редагувати та видаляти.
@login_required
def income_list(request):
    incomes = Income.objects.filter(user=request.user)
   
    # Фільтрація за описом
    description = request.GET.get("description")
    if description:
        incomes = incomes.filter(description=description)

    # Фільтрація за датою
    date_from = request.GET.get("date_from", "")
    date_to = request.GET.get("date_to", "")
    if date_from:
        incomes = incomes.filter(date__gte=datetime.strptime(date_from, "%Y-%m-%d"))
    if date_to:
        incomes = incomes.filter(date__lte=datetime.strptime(date_to, "%Y-%m-%d"))

    # Сортування
    sort_by = request.GET.get("sort_by", "")
    if sort_by == "amount":
        incomes = incomes.order_by("amount")
    elif sort_by == "date":
        incomes = incomes.order_by("date")
        
    return render(request, "incomes/income_list.html", {"incomes": incomes})


@login_required
def add_income(request):
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
    income = get_object_or_404(Income, pk=pk, user=request.user)
    if request.method == "POST":
        income.delete()
        return redirect("incomes:income_list")
    return render(request, "incomes/income_confirm_delete.html", {"income": income})

@login_required
def delete_all_incomes(request):
    if request.method == "POST":
        Income.objects.filter(user=request.user).delete()
        return redirect("incomes:income_list")
    return render(request, "incomes/delete_all_incomes.html")
