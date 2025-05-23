# Generated by Django 5.1.6 on 2025-04-22 01:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Valor')),
                ('category', models.IntegerField(choices=[(1, 'Vestuário'), (2, 'Dívidas'), (3, 'Educação'), (4, 'Alimentação'), (5, 'Presentes'), (6, 'Saúde'), (7, 'Moradia'), (8, 'Investimentos'), (9, 'Lazer'), (10, 'Pets'), (11, 'Tecnologia'), (12, 'Transporte'), (13, 'Outros')], verbose_name='Categoria')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Data')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Descrição')),
                ('destination', models.CharField(max_length=55, verbose_name='Destino')),
                ('is_paid', models.BooleanField(default=True, verbose_name='Pago?')),
                ('transaction_type', models.IntegerField(choices=[(1, 'Saída'), (2, 'Entrada')], verbose_name='Tipo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Editado em')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', related_query_name='transaction', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
