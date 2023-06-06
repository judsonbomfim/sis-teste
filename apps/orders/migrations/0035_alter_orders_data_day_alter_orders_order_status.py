# Generated by Django 4.2 on 2023-06-06 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0034_alter_orders_data_day_alter_orders_order_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='data_day',
            field=models.CharField(choices=[('ilimitado', 'Ilimitado'), ('2gb', '2GB'), ('500mb-dia', '500GB'), ('1gb', '1GB')], max_length=15),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_status',
            field=models.CharField(choices=[('RP', 'Reprocessar'), ('AT', 'Ativado'), ('CC', 'Cancelado'), ('PR', 'Processando'), ('RB', 'Reembolsado')], default='PR', max_length=2),
        ),
    ]
