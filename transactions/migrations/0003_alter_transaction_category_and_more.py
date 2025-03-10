# Generated by Django 5.1.6 on 2025-03-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_alter_transaction_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.IntegerField(choices=[(1, 'Vestuário'), (2, 'Dívidas'), (3, 'Educação'), (4, 'Alimentação'), (5, 'Presentes'), (6, 'Saúde'), (7, 'Moradia'), (8, 'Investimentos'), (9, 'Lazer'), (10, 'Pets'), (11, 'Tecnologia'), (12, 'Transporte'), (13, 'Outros')], verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='is_paid',
            field=models.BooleanField(default=True, verbose_name='Pago?'),
        ),
    ]
