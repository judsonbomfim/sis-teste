# Generated by Django 4.2 on 2023-06-06 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_alter_orders_data_day_alter_orders_order_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='data_day',
            field=models.CharField(choices=[('2gb', '2GB'), ('1gb', '1GB'), ('500mb-dia', '500GB'), ('ilimitado', 'Ilimitado')], max_length=15),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_status',
            field=models.CharField(choices=[('AT', 'Ativado'), ('RB', 'Reembolsado'), ('RP', 'Reprocessar'), ('CC', 'Cancelado'), ('PR', 'Processando')], default='PR', max_length=2),
        ),
        migrations.AlterField(
            model_name='orders',
            name='product',
            field=models.CharField(choices=[('chip-internacional-europa', 'EUROPA'), ('chip-internacional-eua', 'USA'), ('chip-internacional-global', 'GLOBAL PREMIUM'), ('chip-internacional-eua-e-canada', 'USA e CANADA')], max_length=35),
        ),
    ]
