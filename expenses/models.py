from django.db import models
from django.utils.translation import gettext_lazy as _

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ("food", "Food"),
        ("transport", "Transport"),
        ("entertainment", "Entertainment"),
        ("bills", "Bills"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=255, verbose_name=_("Expense Name"))  # Назва витрати
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сума
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  # Категорія
    date = models.DateField()  # Дата створення

    def __str__(self):
        return f"{self.name} - {self.amount} USD"
