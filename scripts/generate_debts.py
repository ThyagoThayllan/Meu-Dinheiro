import django
import os
import random
import sys
from faker import Faker
from pathlib import Path


DJANGO_BASE_DIR = Path(__file__).parent.parent

sys.path.append(str(DJANGO_BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meu_dinheiro.settings')

django.setup()


from debts.models import Debt
from django.contrib.auth import get_user_model


fake = Faker('pt_BR')

User = get_user_model()

users = User.objects.all()

for _ in range(100):
    installments = random.randint(1, 120)
    installments_paid = random.randint(1, installments)
    is_paid = installments == installments_paid

    Debt.objects.create(
        amount=fake.pydecimal(
            left_digits=5, right_digits=2, positive=True, min_value=500, max_value=100000
        ),
        category=random.choice(Debt.DEBT_CATEGORIES)[0],
        description=fake.bank_country(),
        financier=fake.bank_country(),
        installments=installments,
        installments_paid=installments_paid,
        is_paid=is_paid,
        user=random.choice(users),
    )
