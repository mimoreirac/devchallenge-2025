from django.urls import path
from . import views
from .views import AnuncioDetalleView

urlpatterns = [
    path("", views.tablero_principal, name="tablero_principal"),
    path("anuncios/<int:pk>/", AnuncioDetalleView.as_view(), name="detalle-anuncio"),
]
