from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Anuncio(models.Model):
    class Sectores(models.TextChoices):
        NORTE = "NORTE", "Norte"
        SUR = "SUR", "Sur"
        CENTRO = "CENTRO", "Centro"
        VALLE_CHILLOS = "VALLE CHILLOS", "Valle de los Chillos"
        CUMBAYA = "CUMBAYA", "Cumbayá"
        TUMBACO = "TUMBACO", "Tumbaco"

    conductor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sector = models.CharField(max_length=50, choices=Sectores.choices)
    hora_salida = models.TimeField()
    hora_llegada = models.TimeField()
    desde_donde = models.CharField(max_length=100)
    hacia_donde = models.CharField(max_length=100)
    numero_contacto = PhoneNumberField(region="EC")

    def __str__(self):
        return f"Anuncio de {self.conductor.get_username()} desde {self.desde_donde} hacia {self.hacia_donde}"
