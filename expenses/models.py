from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Expense(models.Model):
    class CategoryChoices(models.TextChoices):
        FOOD = "food", _("Food")
        TRANSPORT = "transport", _("Transport")
        ENTERTAINMENT = "entertainment", _("Entertainment")
        BILLES = "bills", _("Bills")
        OTHER = "other", _("Other")

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Зв'язок з користувачем
    name = models.CharField(
        max_length=255, verbose_name=_("Expense Name")
    )  # Назва витрати
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Amount")
    )  # Сума
    category = models.CharField(
        max_length=20, choices=CategoryChoices.choices, verbose_name=_("Category")
    )  # Категорія
    date = models.DateField(verbose_name=_("Date"))  # Дата створення

    class Meta:
        verbose_name = _("Expense")
        verbose_name_plural = _("Expenses")
        ordering = ["-date"]

    def __str__(self):
        return f"{self.name} - {self.amount}"
