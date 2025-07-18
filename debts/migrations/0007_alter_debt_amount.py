# Generated by Django 5.1.6 on 2025-06-15 22:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debts', '0006_alter_debt_amount_alter_debt_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MaxValueValidator(99999999.99), django.core.validators.MinValueValidator(0.01)], verbose_name='Valor da Dívida'),
        ),
    ]
