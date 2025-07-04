from django.urls import path
from .views import AnuncioCreateView, AnuncioListView, AnuncioUpdateView, AnuncioDetalleView

urlpatterns = [
    path("", AnuncioListView.as_view(), name="tablero"),
    path("anuncios/crear/", AnuncioCreateView.as_view(), name="crear_anuncio"),
    path("anuncios/<int:pk>/editar/", AnuncioUpdateView.as_view(), name="editar_anuncio"),
    path("anuncios/<int:pk>/", AnuncioDetalleView.as_view(), name="detalle_anuncio"),
]