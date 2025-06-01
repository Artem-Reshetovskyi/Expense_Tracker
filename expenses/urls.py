from django.urls import path

from . import views

app_name = "expenses"

urlpatterns = [
    path("add/", views.add_expense, name="add_expense"),
    path("", views.expense_list, name="expense_list"),
    path("edit/<int:pk>/", views.edit_expense, name="edit_expense"),
    path("delete/<int:pk>/", views.delete_expense, name="delete_expense"),
    path("delete_all/", views.delete_all_expenses, name="delete_all_expenses"),
]
