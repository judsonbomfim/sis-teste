from django.db import models

SIM_STATUS = {
    ('DS', 'Disponível'),
    ('AT', 'Ativado'),
    ('CC', 'Cancelado'),
}
OPERATOR = {
    ('TM', 'T-Mobile'), 
    ('CM', 'China Mobile'),
    ('TC', 'Telcom'), 
}
TYPES = {
    ('sim', 'SIM (Físico)'),   
    ('esim', 'eSIM (Virtual)'),   
}

class Sims(models.Model):
    id = models.IntegerField(primary_key=True)
    sim = models.CharField(max_length=20)
    link = models.URLField(null=True, blank=True)
    type =  models.CharField(max_length=4, choices=TYPES)
    operator = models.CharField(max_length=2, choices=OPERATOR)
    sim_status = models.CharField(max_length=2, choices=SIM_STATUS, default='DS')