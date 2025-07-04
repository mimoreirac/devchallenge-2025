from django.shortcuts import render
from django.views.generic import DetailView
from .models import Anuncio


def tablero_principal(request):
    anuncios = Anuncio.objects.all().order_by("-hora_salida")
    return render(request, "carroscompartidos/tablero.html", {"anuncios": anuncios})


class AnuncioDetalleView(DetailView):
    model = Anuncio
    template_name = "carroscompartidos/anuncio_detalle.html"
    context_object_name = "anuncio"
