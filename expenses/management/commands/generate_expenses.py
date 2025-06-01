from django.core.management.base import BaseCommand
from expenses.models import Expense
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
import random

User = get_user_model()

CATEGORIES = ["food", "transport", "entertainment", "bills", "other"]
NAMES = {
    "food": ["Groceries", "Restaurant", "Coffee", "Supermarket", "Fast Food", "Snacks", "Misc"],
    "transport": ["Bus", "Train", "Fuel", "Taxi", "Parking", "Car Rental"],
    "entertainment": ["Movies", "Games", "Subscription", "Concert", "Books", "Hobby", "Misc"],
    "bills": ["Electricity", "Internet", "Water", "Phone", "Rent", "Gas"],
    "other": ["Gift", "Clothing", "Health", "Education", "Travel", "Charity", "Miscellaneous"],
}


class Command(BaseCommand):
    help = "Generate simulated expenses for 3 months"

    def handle(self, *args, **kwargs):
        start_date = datetime(2025, 3, 1)
        end_date = datetime(2025, 5, 30)
        delta_days = (end_date - start_date).days

        user = User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR("No users found."))
            return

        for _ in range(100):  # згенерує 100 витрат
            date = start_date + timedelta(days=random.randint(0, delta_days))
            category = random.choice(CATEGORIES)
            name = random.choice(NAMES[category])
            amount = round(random.uniform(5, 100), 2)

            Expense.objects.create(
                user=user,
                amount=amount,
                category=category,
                name=name,
                date=date,
            )

        self.stdout.write(self.style.SUCCESS("✅ 100 expenses created."))
