from django.contrib import admin
from .models import Anuncio


@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ("conductor", "sector", "desde_donde", "hacia_donde")
