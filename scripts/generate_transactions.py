import django
import os
import random
import sys
from datetime import date
from faker import Faker
from pathlib import Path


DJANGO_BASE_DIR = Path(__file__).parent.parent

sys.path.append(str(DJANGO_BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meu_dinheiro.settings')

django.setup()


from transactions.models import Transaction
from django.contrib.auth import get_user_model


fake = Faker('pt_BR')

User = get_user_model()

users = User.objects.all()

for _ in range(100):
    Transaction.objects.create(
        amount=fake.pydecimal(
            left_digits=4,
            max_value=1000,
            min_value=500,
            positive=True,
            right_digits=2,
        ),
        category=random.choice(Transaction.CATEGORIES)[0],
        date=fake.date_between(
            end_date=date(day=31, month=12, year=2025),
            start_date=date(day=1, month=1, year=2025),
        ),
        description=fake.bank_country(),
        destination=fake.name(),
        is_paid=fake.boolean(),
        transaction_type=random.choice(Transaction.TRANSACTION_TYPES)[0],
        user=random.choice(users),
    )
