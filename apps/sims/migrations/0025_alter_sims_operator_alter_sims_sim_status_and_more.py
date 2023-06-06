# Generated by Django 4.2 on 2023-06-06 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0024_alter_sims_sim_status_alter_sims_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sims',
            name='operator',
            field=models.CharField(choices=[('CM', 'China Mobile'), ('TC', 'Telcom'), ('TM', 'T-Mobile')], max_length=2),
        ),
        migrations.AlterField(
            model_name='sims',
            name='sim_status',
            field=models.CharField(choices=[('DS', 'Disponível'), ('AT', 'Ativado'), ('CC', 'Cancelado')], default='DS', max_length=2),
        ),
        migrations.AlterField(
            model_name='sims',
            name='type',
            field=models.CharField(choices=[('esim', 'eSIM (Virtual)'), ('sim', 'SIM (Físico)')], max_length=4),
        ),
    ]
