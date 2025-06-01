from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Income


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = [
            "amount",
            "description",
            "date",
        ]
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
