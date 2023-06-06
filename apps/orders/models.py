from django.db import models
from django.contrib.auth.models import User
from apps.sims.models import Sims

PRODUCT = {
    ('chip-internacional-eua', 'USA'),
    ('chip-internacional-eua-e-canada', 'USA e CANADA'),
    ('chip-internacional-europa', 'EUROPA'),
    ('chip-internacional-global', 'GLOBAL PREMIUM'),
}

DATA = {
    ('500mb-dia', '500GB'),
    ('1gb', '1GB'),
    ('2gb', '2GB'),
    ('ilimitado', 'Ilimitado'),
}

ORDER_STATUS = {
    ('AT', 'Ativado'),
    ('CC', 'Cancelado'),
    ('RB', 'Reembolsado'),
    ('RP', 'Reprocessar'),
    ('PR', 'Processando'),
}
CONDITION = {
    ('novo-sim', 'Novo SIM'),
    ('reuso-sim', 'Reutilizar'),
}

class Orders(models.Model):
    order_id = models.IntegerField()
    item_id = models.CharField(max_length=15)
    client = models.CharField(max_length=70)
    product = models.CharField(max_length=35, choices=PRODUCT)
    data_day = models.CharField(max_length=15, choices=DATA)
    qty = models.IntegerField()
    coupon = models.CharField(max_length=15, default=None)
    days = models.IntegerField()
    calls = models.BooleanField(default=False)
    countries = models.BooleanField(default=False)
    cell_mod = models.CharField(max_length=35)
    ord_chip_nun = models.CharField(max_length=25, null=True, blank=True, default='-')
    shipping = models.CharField(max_length=35)
    order_date = models.DateTimeField()
    activation_date = models.DateField()
    order_status = models.CharField(max_length=2, choices=ORDER_STATUS, default='PR')
    id_sim = models.ForeignKey(Sims, on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    condition = models.CharField(max_length=15, default='novo-sim') 
    notes = models.IntegerField(null=True, blank=True, default=0)

class Notes(models.Model):
    id_pedido = models.ForeignKey(Orders, on_delete=models.DO_NOTHING, related_name='note')
    id_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data = models.DateField()