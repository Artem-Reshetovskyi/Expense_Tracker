from django.core.management.base import BaseCommand
from expenses.models import Income
from django.contrib.auth import get_user_model
from datetime import datetime
from calendar import monthrange
import random

User = get_user_model()

description_choices = Income.DescriptionChoices

INCOME_SOURCES = {
    Income.DescriptionChoices.SALARY: (3000, 5000),
    Income.DescriptionChoices.BONUS: (200, 800),
    Income.DescriptionChoices.FREELANCE: (500, 1500),
    Income.DescriptionChoices.OTHER: (50, 500),
    Income.DescriptionChoices.INVESTMENT: (100, 1000),
    Income.DescriptionChoices.RENT: (800, 2000),
}


class Command(BaseCommand):
    help = "Generate simulated incomes for 3 months"

    def handle(self, *args, **kwargs):
        months = [3, 4, 5]  # Березень, Квітень, Травень
        year = 2025

        user = User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR("❌ No user found."))
            return

        # Трекер для унікальних доходів в кожному місяці
        used_types_per_month = {month: set() for month in months}

        incomes_created = 0

        # Спершу обов’язково додаємо SALARY для кожного місяця
        for month in months:
            amount_range = INCOME_SOURCES[Income.DescriptionChoices.SALARY]
            amount = round(random.uniform(*amount_range), 2)
            day = random.choice([8, 9])
            date = datetime(year, month, day)

            Income.objects.create(
                user=user,
                amount=amount,
                description=Income.DescriptionChoices.SALARY,
                date=date,
            )
            used_types_per_month[month].add(Income.DescriptionChoices.SALARY)
            incomes_created += 1

        # Тепер додаємо інші доходи, уникаючи дублікатів в кожному місяці
        attempts = 0
        max_attempts = 50  # щоб не зациклитись

        while incomes_created < 15 and attempts < max_attempts:
            attempts += 1

            # Вибираємо випадковий місяць
            month = random.choice(months)

            # Вибираємо випадковий тип доходу
            desc_choice = random.choice(list(INCOME_SOURCES.keys()))

            # SALARY ми вже додали, тому пропускаємо, якщо випав знову
            if desc_choice == Income.DescriptionChoices.SALARY:
                continue

            # Перевіряємо обмеження: унікальність для певних типів доходів
            if desc_choice in [
                Income.DescriptionChoices.BONUS,
                Income.DescriptionChoices.INVESTMENT,
                Income.DescriptionChoices.RENT,
            ]:
                if desc_choice in used_types_per_month[month]:
                    continue  # цей тип доходу вже є в цьому місяці — беремо інший

            amount_range = INCOME_SOURCES[desc_choice]
            amount = round(random.uniform(*amount_range), 2)

            if desc_choice == Income.DescriptionChoices.BONUS:
                day = random.choice([23, 24])
            elif desc_choice == Income.DescriptionChoices.INVESTMENT:
                day = random.randint(1, 5)
            elif desc_choice == Income.DescriptionChoices.RENT:
                day = random.randint(10, 12)
            else:
                last_day = monthrange(year, month)[1]
                day = random.randint(1, last_day)

            date = datetime(year, month, day)

            Income.objects.create(
                user=user, amount=amount, description=desc_choice, date=date
            )

            # Позначаємо цей тип доходу як використаний для цього місяця
            if desc_choice in [
                Income.DescriptionChoices.BONUS,
                Income.DescriptionChoices.INVESTMENT,
                Income.DescriptionChoices.RENT,
            ]:
                used_types_per_month[month].add(desc_choice)

            incomes_created += 1

        if incomes_created < 15:
            self.stdout.write(
                self.style.WARNING(
                    f"⚠️ Only {incomes_created} incomes were created after {attempts} attempts"
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS("✅ 15 simulated incomes were created.")
            )
