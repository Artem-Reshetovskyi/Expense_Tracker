from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Income


class IncomeForm(forms.ModelForm):
    """
    Form for creating and updating Income instances.

    Includes fields for amount, description, and date.
    The date field uses an HTML5 date input widget.
    The description field prepends an empty choice prompting the user to select.
    """

    class Meta:
        """
        Meta options for IncomeForm.

        Attributes:
            model (Model): The model associated with this form (Income).
            fields (list[str]): Fields included in the form.
            labels (dict): Human-readable labels for the fields.
            widgets (dict): Custom widgets for form fields.
        """

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
        """
        Initialize the form and prepend a default empty choice to the description field.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.fields["description"].choices = [("", _("Choose..."))] + list(
            self.fields["description"].choices
        )
