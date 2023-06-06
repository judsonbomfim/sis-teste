# Generated by Django 4.2 on 2023-06-06 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0018_alter_sims_type'),
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