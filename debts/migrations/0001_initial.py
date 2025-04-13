# Generated by Django 5.1.6 on 2025-04-13 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Valor da Dívida')),
                ('category', models.IntegerField(choices=[(3, 'Cartão de Crédito'), (4, 'Financiamento'), (5, 'Empréstimo'), (6, 'Pessoal'), (7, 'Cheque Especial'), (8, 'Outros')], verbose_name='Categoria')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('description', models.CharField(max_length=255, verbose_name='Descrição')),
                ('financier', models.CharField(max_length=55, verbose_name='Financiador')),
                ('installments', models.IntegerField(verbose_name='Parcelas')),
                ('installments_paid', models.IntegerField(verbose_name='Parcelas Pagas')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Paga?')),
                ('status', models.IntegerField(choices=[(1, 'Ativa'), (2, 'Inativa')], verbose_name='Status da Dívida')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Editado em')),
            ],
        ),
    ]
