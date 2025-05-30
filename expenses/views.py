from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from .models import Income
from .forms import IncomeForm
from django.db.models import Q
from datetime import datetime
from django.contrib.auth.decorators import login_required # Декоратор для захисту від неавторизованого доступу  

#Expense - це витрати, які користувач може додавати, редагувати та видаляти.
    # Відображення списку витрат з можливістю фільтрації та сортування
@login_required 
def expense_list(request):
    expenses = Expense.objects.all()  # За замовчуванням беремо всі витрати
    category = request.GET.get("category")  # Отримуємо категорію з параметрів URL
    sort_by = request.GET.get("sort_by")  # Отримуємо параметр для сортування

    # Фільтруємо за категорією
    if category:
        expenses = expenses.filter(category=category)

    # Фільтруємо за датою
    date_from = request.GET.get("date_from", "")
    date_to = request.GET.get("date_to", "")
    if date_from:
        expenses = expenses.filter(date__gte=datetime.strptime(date_from, "%Y-%m-%d"))
    if date_to:
        expenses = expenses.filter(date__lte=datetime.strptime(date_to, "%Y-%m-%d"))

    # Сортування
    sort_by = request.GET.get("sort_by", "")
    if sort_by == "amount":
        expenses = expenses.order_by("amount")
    elif sort_by == "date":
        expenses = expenses.order_by("date")

    return render(request, "expenses/expense_list.html", {"expenses": expenses})


@login_required  # Додаємо захист для функції додавання витрат
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()  # Зберігаємо нову витрату в базу даних
            return redirect("expense_list")  # Повертаємося на список витрат
    else:
        form = ExpenseForm()

    return render(request, "expenses/add_expense.html", {"form": form})


@login_required  # Додаємо захист для функції редагування витрат
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)  # Отримуємо витрату або повертаємо 404
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)  # Форма із заповненими даними
        if form.is_valid():
            form.save()  # Зберігаємо зміни
            return redirect("expense_list")  # Повертаємося до списку витрат
    else:
        form = ExpenseForm(instance=expense)  # Заповнюємо форму поточними даними
    return render(request, "expenses/edit_expense.html", {"form": form, "expense": expense})


@login_required  # Додаємо захист для функції видалення витрат
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == "POST":
        expense.delete()
        return redirect("expense_list")

    return render(request, "expenses/delete_expense.html", {"expense": expense})


@login_required  # Додаємо захист для функції видалення всіх витрат
def delete_all_expenses(request):
    if request.method == "POST":
        Expense.objects.all().delete()
        return redirect("expense_list")

    return render(request, "expenses/delete_all_expenses.html")

# Incomes - це доходи користувача, які він може додавати, редагувати та видаляти.
@login_required
def income_list(request):
    incomes = Income.objects.filter(user=request.user)
    return render(request, "incomes/income_list.html", {"incomes": incomes})


@login_required
def income_create(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect("income_list")
    else:
        form = IncomeForm()
    return render(request, "incomes/income_form.html", {"form": form})


@login_required
def income_edit(request, pk):
    income = Income.objects.get(pk=pk, user=request.user)
    if request.method == "POST":
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect("income_list")
    else:
        form = IncomeForm(instance=income)
    return render(request, "incomes/income_form.html", {"form": form})


@login_required
def income_delete(request, pk):
    income = Income.objects.get(pk=pk, user=request.user)
    if request.method == "POST":
        income.delete()
        return redirect("income_list")
    return render(request, "incomes/income_confirm_delete.html", {"income": income})

@login_required
def delete_all_incomes(request):
    if request.method == "POST":
        Income.objects.all().delete()
        return redirect("income_list")
    return render(request, "incomes/delete_all_incomes.html")