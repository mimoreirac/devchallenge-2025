from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Anuncio
from .forms import AnuncioForm


class AnuncioListView(ListView):
    model = Anuncio
    template_name = "carroscompartidos/tablero.html"
    context_object_name = "anuncios"
    ordering = ["hora_salida"]


class AnuncioCreateView(LoginRequiredMixin, CreateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = "carroscompartidos/anuncio_form.html"
    success_url = reverse_lazy("tablero")

    def form_valid(self, form):
        form.instance.conductor = self.request.user
        return super().form_valid(form)


class AnuncioUpdateView(LoginRequiredMixin, UpdateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = "carroscompartidos/anuncio_form.html"
    success_url = reverse_lazy("tablero")

    def get_queryset(self):
        return self.model.objects.filter(conductor=self.request.user)


class AnuncioDetalleView(DetailView):
    model = Anuncio
    template_name = "carroscompartidos/anuncio_detalle.html"
    context_object_name = "anuncio"
