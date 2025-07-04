from django.urls import path
from .views import AnuncioCreateView, AnuncioUpdateView, AnuncioListView

urlpatterns = [
    path("", AnuncioListView.as_view(), name="anuncio-list"),
    path("anuncios/crear/", AnuncioCreateView.as_view(), name="anuncio-create"),
    path(
        "anuncios/<int:pk>/editar/", AnuncioUpdateView.as_view(), name="anuncio-update"
    ),
]
