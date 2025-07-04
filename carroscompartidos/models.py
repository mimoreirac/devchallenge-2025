from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Anuncio(models.Model):
    conductor = models.CharField(max_length=100)
    SECTORES = {
        "NORTE": "Norte",
        "SUR": "Sur",
        "CENTRO": "Centro",
        "VALLE CHILLOS": "Valle de los Chillos",
        "CUMBAYA": "Cumbayá",
        "TUMBACO": "Tumbaco",
    }
    sector = models.CharField(max_length=50, choices=SECTORES)
    hora_salida = models.TimeField()
    hora_llegada = models.TimeField()
    desde_donde = models.CharField(max_length=100)
    hacia_donde = models.CharField(max_length=100)
    numero_contacto = PhoneNumberField(region="EC")
