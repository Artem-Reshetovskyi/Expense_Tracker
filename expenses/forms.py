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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].choices = [("", _("Chooce..."))] + list(
            self.fields["category"].choices
        )


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ["amount", "description", "date",]
        labels = {
            "amount": _("Amount"),
            "description": _("Description"),
            "date": _("Date"),
        }
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].choices = [("", _("Chooce..."))] + list(
            self.fields["description"].choices
        )
