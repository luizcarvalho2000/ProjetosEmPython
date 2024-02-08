# Generated by Django 4.2.5 on 2023-09-17 17:55

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_rename_nome_servico_servico_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='preco',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='precos', to='appointments.servico'),
        ),
    ]
