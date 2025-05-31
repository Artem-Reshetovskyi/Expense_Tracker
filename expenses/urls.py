from django.urls import path
from . import views

urlpatterns = [
    path("", views.expense_list, name="expense_list"),
    path("add/", views.add_expense, name="add_expense"),
    path("edit/<int:expense_id>/", views.edit_expense, name="edit_expense"),
    path("delete/<int:expense_id>/", views.delete_expense, name="delete_expense"),
    path("delete_all/", views.delete_all_expenses, name="delete_all_expenses"),
    path("incomes/", views.income_list, name="income_list"),
    path("incomes/create/", views.income_create, name="income_create"),
    path("incomes/edit/<int:pk>/", views.income_edit, name="income_edit"),
    path("incomes/delete/<int:pk>/", views.income_delete, name="income_delete"),
]
