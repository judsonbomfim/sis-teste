# Generated by Django 4.2 on 2023-06-06 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0007_alter_sims_operator_alter_sims_sim_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sims',
            name='operator',
            field=models.CharField(choices=[('TM', 'T-Mobile'), ('TC', 'Telcom'), ('CM', 'China Mobile')], max_length=2),
        ),
        migrations.AlterField(
            model_name='sims',
            name='sim_status',
            field=models.CharField(choices=[('AT', 'Ativado'), ('CC', 'Cancelado'), ('DS', 'Disponível')], default='DS', max_length=2),
        ),
    ]
