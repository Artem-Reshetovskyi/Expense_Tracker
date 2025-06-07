from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Income(models.Model):
    """
    Model representing an income entry linked to a user.

    Attributes:
        user (ForeignKey): Reference to the user who owns this income record.
        amount (DecimalField): The amount of the income.
        description (CharField): The type or source of the income,
            chosen from predefined description choices.
        date (DateField): The date the income was recorded.
    """

    class DescriptionChoices(models.TextChoices):
        """Predefined choices for income description."""

        SALARY = "salary", _("Salary")
        BONUS = "bonus", _("Bonus")
        INVESTMENT = "investment", _("Investment")
        FREELANCE = "freelance", _("Freelance")
        RENT = "rent", _("Rent")
        SALE = "sale", _("Sale")
        OTHER = "other", _("Other")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(
        max_length=50,
        choices=DescriptionChoices.choices,
        blank=True,
        null=True,
        verbose_name=_("Description"),
    )
    date = models.DateField()

    class Meta:
        verbose_name = _("Income")
        verbose_name_plural = _("Incomes")
        ordering = ["-date"]

    def __str__(self):
        """
        Returns a human-readable string representation of the income.

        Returns:
            str: Formatted string showing amount and description.
        """
        return f"{self.amount} - {self.get_description_display()}"
