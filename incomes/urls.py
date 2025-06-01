from django.urls import path

from . import views

app_name = "incomes"

urlpatterns = [
    path("", views.income_list, name="income_list"),
    path("add/", views.add_income, name="add_income"),
    path("edit/<int:pk>/", views.income_edit, name="income_edit"),
    path("delete/<int:pk>/", views.income_delete, name="income_delete"),
    path("delete_all/", views.delete_all_incomes, name="delete_all_incomes"),
]
