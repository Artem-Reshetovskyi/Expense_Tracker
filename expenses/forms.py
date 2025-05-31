from django import forms
from .models import Expense
from .models import Income
from django.utils.translation import gettext_lazy as _


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = [
            "name",
            "amount",
            "category",
            "date",
        ]  # Поля, які можна заповнювати у формі
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"})  # Поле для вибору дати
        }


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ["amount", "description", "date"]
        labels = {
            "amount": _("Amount"),
            "description": _("Description"),
            "date": _("Date"),
        }
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }
