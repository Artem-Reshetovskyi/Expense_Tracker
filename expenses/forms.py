from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Expense


class ExpenseForm(forms.ModelForm):
    """
    Form for creating and updating Expense instances.

    Provides fields to input expense details including name, amount,
    category, and date. The date field uses an HTML5 date input widget.
    The category field includes a default empty choice prompting the user
    to select a category.
    """

    class Meta:
        """
        Meta options for ExpenseForm.

        Attributes:
            model (Model): The model associated with this form (Expense).
            fields (list[str]): List of model fields included in the form.
            widgets (dict): Custom widgets for form fields.
        """

        model = Expense
        fields = [
            "name",
            "amount",
            "category",
            "date",
        ]
        widgets = {"date": forms.DateInput(attrs={"type": "date"})}

    def __init__(self, *args, **kwargs):
        """
        Initialize the form and prepend a default choice to the category field.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.fields["category"].choices = [("", _("Choose..."))] + list(
            self.fields["category"].choices
        )
