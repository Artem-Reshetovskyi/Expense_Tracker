from django.test import TestCase
from .models import Expense
from datetime import date


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


