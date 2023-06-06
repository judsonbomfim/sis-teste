# Generated by Django 4.2 on 2023-06-06 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0021_alter_sims_operator_alter_sims_sim_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sims',
            name='sim_status',
            field=models.CharField(choices=[('AT', 'Ativado'), ('CC', 'Cancelado'), ('DS', 'Disponível')], default='DS', max_length=2),
        ),
        migrations.AlterField(
            model_name='sims',
            name='type',
            field=models.CharField(choices=[('sim', 'SIM (Físico)'), ('esim', 'eSIM (Virtual)')], max_length=4),
        ),
    ]
