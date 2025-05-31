from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ("food", _("Food")),
        ("transport", _("Transport")),
        ("entertainment", _("Entertainment")),
        ("utilities", _("Utilities")),
        ("other", _("Other")),
    ]
    name = models.CharField(max_length=255, verbose_name=_("Expense Name"))  # Назва витрати
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Amount"))  # Сума
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name=_("Category"))  # Категорія
    date = models.DateField(verbose_name=_("Date"))  # Дата створення

    def __str__(self):
        return f"{self.name} - {self.amount}"


class Income(models.Model):
    class Description(models.TextChoices):
        SALARY = "salary", _("Salary")
        BONUS = "bonus", _("Bonus")
        INVESTMENT = "investment", _("Investment")
        RENT = "rent", _("Rent")
        SALE = "sale", _("Sale")
        OTHER = "other", _("Other")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=50, choices=Description.choices, default=Description.OTHER)
    date = models.DateField()

    class Meta:
        verbose_name = _("Income")
        verbose_name_plural = _("Incomes")
        ordering = ["-date"]

    def __str__(self):
        return f"{self.amount} - {self.get_description_display()}"