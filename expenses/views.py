from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Q


def expense_list(request):
    category = request.GET.get("category")  # Отримуємо категорію з параметрів URL
    sort_by = request.GET.get("sort_by")  # Отримуємо параметр для сортування
    expenses = Expense.objects.all()  # За замовчуванням беремо всі витрати

    if category:
        expenses = expenses.filter(
            category=category
        )  # Фільтруємо за категорією, якщо вона передана
    if sort_by:
        if sort_by == "amount":
            expenses = expenses.order_by("amount")  # Сортуємо за сумою
        elif sort_by == "date":
            expenses = expenses.order_by("date")  # Сортуємо за датою

    return render(request, "expenses/expense_list.html", {"expenses": expenses})


def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()  # Зберігаємо нову витрату в базу даних
            return redirect("expense_list")  # Повертаємося на список витрат
    else:
        form = ExpenseForm()

    return render(request, "expenses/add_expense.html", {"form": form})


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


def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == "POST":
        expense.delete()  # Видаляємо витрату
        return redirect("expense_list")

    return render(request, "expenses/delete_expense.html", {"expense": expense})


def delete_all_expenses(request):
    if request.method == "POST":
        Expense.objects.all().delete()
        return redirect("expense_list")

    return render(request, "expenses/delete_all_expenses.html")
