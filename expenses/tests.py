from django.test import TestCase
from .models import Expense
from datetime import date
from .forms import ExpenseForm


class ExpenseModelTest(TestCase):
    """
    Test dla modelu Expense.
    """
    def test_expense_str(self):
        expense = Expense.objects.create(
            name="Kebsik",
            amount=25.50,
            category="food",
            date=date.today()
        )
        self.assertEqual(str(expense), "Kebsik - 25.5")


class ExpenseFormTest(TestCase):
    """
    Test walidacji dla formularza ExpenseForm.
    """
    def test_valid_form(self):
        form_data = {
            "name": "Bilet na tramwaj",
            "amount": 3.50,
            "category": "transport",
            "date": "2025-06-04",
        }
        form = ExpenseForm(data=form_data)
        self.assertTrue(form.is_valid())