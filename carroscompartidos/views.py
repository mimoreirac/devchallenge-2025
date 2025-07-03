from django.shortcuts import render
from .models import Anuncio  

def tablero_principal(request):
    anuncios = Anuncio.objects.all().order_by('-hora_salida') 
    return render(request, 'carroscompartidos/tablero.html', {'anuncios': anuncios})
