from django.core.management.base import BaseCommand
from incomes.models import Income, DescriptionChoices 
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
import random

User = get_user_model()

INCOME_SOURCES = {
    DescriptionChoices.SALARY: (3000, 5000),
    DescriptionChoices.BONUS: (200, 800),
    DescriptionChoices.FREELANCE: (500, 1500),
    DescriptionChoices.OTHER: (50, 500),
    DescriptionChoices.INVESTMENT: (100, 1000),
    DescriptionChoices.RENT: (800, 2000),
}


class Command(BaseCommand):
    help = "Generate simulated incomes for 3 months"

    def handle(self, *args, **kwargs):
        start_date = datetime(2025, 3, 1)
        end_date = datetime(2025, 5, 30)
        delta_days = (end_date - start_date).days

        user = User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR("❌ No user found."))
            return

        for _ in range(15):  # Створимо 15 випадкових доходів
            date = start_date + timedelta(days=random.randint(0, delta_days))
            desc_choice = random.choice(list(INCOME_SOURCES.keys()))
            amount_range = INCOME_SOURCES[desc_choice]
            amount = round(random.uniform(*amount_range), 2)

            Income.objects.create(
                user=user, amount=amount, description=desc_choice, date=date
            )

        self.stdout.write(self.style.SUCCESS("✅ 15 simulated incomes were created."))
