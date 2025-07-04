from django import forms
from django.utils.translation import gettext_lazy as _
from allauth.account.forms import SignupForm
from .models import Anuncio


class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        exclude = ("conductor",)
        fields = [
            "desde_donde",
            "hacia_donde",
            "hora_salida",
            "hora_llegada",
            "sector",
            "numero_contacto",
        ]
        widgets = {
            "desde_donde": forms.TextInput(attrs={"class": "form-control"}),
            "hacia_donde": forms.TextInput(attrs={"class": "form-control"}),
            "hora_salida": forms.TimeInput(
                attrs={"class": "form-control", "type": "time"}
            ),
            "hora_llegada": forms.TimeInput(
                attrs={"class": "form-control", "type": "time"}
            ),
            "sector": forms.Select(attrs={"class": "form-select"}),
            "numero_contacto": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "ej, 0991234567"}
            ),
        }


class CustomSignupForm(SignupForm):
    def clean_email(self):
        email = super().clean_email()
        if email and not email.lower().endswith("@puce.edu.ec"):
            raise forms.ValidationError(
                _("Solo se permiten correos con el dominio @puce.edu.ec"),
                code="invalid_email_domain",
            )
        return email
