# Generated by Django 4.2 on 2023-06-06 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0032_alter_orders_data_day_alter_orders_order_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='data_day',
            field=models.CharField(choices=[('2gb', '2GB'), ('1gb', '1GB'), ('ilimitado', 'Ilimitado'), ('500mb-dia', '500GB')], max_length=15),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_status',
            field=models.CharField(choices=[('AT', 'Ativado'), ('RP', 'Reprocessar'), ('PR', 'Processando'), ('RB', 'Reembolsado'), ('CC', 'Cancelado')], default='PR', max_length=2),
        ),
        migrations.AlterField(
            model_name='orders',
            name='product',
            field=models.CharField(choices=[('chip-internacional-eua-e-canada', 'USA e CANADA'), ('chip-internacional-europa', 'EUROPA'), ('chip-internacional-global', 'GLOBAL PREMIUM'), ('chip-internacional-eua', 'USA')], max_length=35),
        ),
    ]
