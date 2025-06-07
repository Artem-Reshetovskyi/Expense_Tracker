from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Expense(models.Model):
    """
    User expense model.

    Attributes:
        user (ForeignKey): The user to whom the expense belongs.
        name (str): The name of the expense.
        amount (Decimal): The amount of the expense.
        category (str): The category of the expense (limited choices).
        date (date): The date of the expense.

    Inner class:
        CategoryChoices (TextChoices): Possible expense categories.
    """

    class CategoryChoices(models.TextChoices):
        """Expense category choices."""

        FOOD = "food", _("Food")
        TRANSPORT = "transport", _("Transport")
        ENTERTAINMENT = "entertainment", _("Entertainment")
        BILLS = "bills", _("Bills")
        OTHER = "other", _("Other")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name=_("Expense Name"))
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Amount")
    )
    category = models.CharField(
        max_length=20, choices=CategoryChoices.choices, verbose_name=_("Category")
    )
    date = models.DateField(verbose_name=_("Date"))

    class Meta:
        """
        Meta information for the Expense model.
        """

        verbose_name = _("Expense")
        verbose_name_plural = _("Expenses")
        ordering = ["-date"]

    def __str__(self):
        """
        Returns a string representation of the expense.

        Returns:
            str: The name of the expense and its amount.
        """
        return f"{self.name} - {self.amount}"
