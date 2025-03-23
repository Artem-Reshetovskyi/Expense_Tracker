from django import forms
from .models import Expense


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
