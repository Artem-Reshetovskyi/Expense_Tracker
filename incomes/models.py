from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Income(models.Model):
    class DescriptionChoices(models.TextChoices):
        SALARY = "salary", _("Salary")
        BONUS = "bonus", _("Bonus")
        INVESTMENT = "investment", _("Investment")
        FREELANCE = "freelance", _("Freelance")
        RENT = "rent", _("Rent")
        SALE = "sale", _("Sale")
        OTHER = "other", _("Other")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=50, choices=DescriptionChoices.choices, blank=True, null=True, verbose_name=_("Description"))
    date = models.DateField()

    class Meta:
        verbose_name = _("Income")
        verbose_name_plural = _("Incomes")
        ordering = ["-date"]

    def __str__(self):
        return f"{self.amount} - {self.get_description_display()}"
