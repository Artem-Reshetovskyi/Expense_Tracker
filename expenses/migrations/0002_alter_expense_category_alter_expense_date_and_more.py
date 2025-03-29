# Generated by Django 5.1.7 on 2025-03-29 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='expense',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Expense Name'),
        ),
    ]
