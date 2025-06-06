from datetime import datetime

from django.contrib.auth.decorators import \
    login_required  # Декоратор для захисту від неавторизованого доступу
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ExpenseForm
from .models import Expense


# Відображення списку витрат з можливістю фільтрації та сортування
@login_required
def expense_list(request):
    expenses = Expense.objects.filter(
        user=request.user
    )  # За замовчуванням беремо всі витрати
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
            expense = form.save(
                commit=False
            )  # Створюємо об'єкт витрати, але не зберігаємо його ще
            expense.user = request.user  # Прив'язуємо витрату до поточного користувача
            expense.save()  # Зберігаємо витрату в базі даних
            return redirect("expenses:expense_list")
    else:
        form = ExpenseForm()

    return render(request, "expenses/add_expense.html", {"form": form})


@login_required  # Додаємо захист для функції редагування витрат
def edit_expense(request, pk):
    expense = get_object_or_404(Expense, id=pk)  # Отримуємо витрату або повертаємо 404
    if request.method == "POST":
        form = ExpenseForm(
            request.POST, instance=expense
        )  # Форма із заповненими даними
        if form.is_valid():
            form.save()  # Зберігаємо зміни
            return redirect("expenses:expense_list")  # Повертаємося до списку витрат
    else:
        form = ExpenseForm(instance=expense)  # Заповнюємо форму поточними даними
    return render(
        request, "expenses/edit_expense.html", {"form": form, "expense": expense}
    )


@login_required  # Додаємо захист для функції видалення витрат
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, id=pk)
    if request.method == "POST":
        expense.delete()
        return redirect("expenses:expense_list")

    return render(request, "expenses/delete_expense.html", {"expense": expense})


@login_required  # Додаємо захист для функції видалення всіх витрат
def delete_all_expenses(request):
    if request.method == "POST":
        Expense.objects.all().delete()
        return redirect("expenses:expense_list")

    return render(request, "expenses/delete_all_expenses.html")
