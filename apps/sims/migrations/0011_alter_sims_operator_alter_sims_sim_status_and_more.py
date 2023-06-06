# Generated by Django 4.2 on 2023-06-06 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0010_alter_sims_sim_status'),
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
            field=models.CharField(choices=[('CC', 'Cancelado'), ('AT', 'Ativado'), ('DS', 'Disponível')], default='DS', max_length=2),
        ),
        migrations.AlterField(
            model_name='sims',
            name='type',
            field=models.CharField(choices=[('sim', 'SIM (Físico)'), ('esim', 'eSIM (Virtual)')], max_length=4),
        ),
    ]