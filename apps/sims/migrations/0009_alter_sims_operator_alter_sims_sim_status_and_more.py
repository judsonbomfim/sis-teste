# Generated by Django 4.2 on 2023-06-06 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0008_alter_sims_operator_alter_sims_sim_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sims',
            name='operator',
            field=models.CharField(choices=[('CM', 'China Mobile'), ('TM', 'T-Mobile'), ('TC', 'Telcom')], max_length=2),
        ),
        migrations.AlterField(
            model_name='sims',
            name='sim_status',
            field=models.CharField(choices=[('CC', 'Cancelado'), ('AT', 'Ativado'), ('DS', 'Disponível')], default='DS', max_length=2),
        ),
        migrations.AlterField(
            model_name='sims',
            name='type',
            field=models.CharField(choices=[('esim', 'eSIM (Virtual)'), ('sim', 'SIM (Físico)')], max_length=4),
        ),
    ]
