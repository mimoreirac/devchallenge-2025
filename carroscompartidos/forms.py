from django import forms
from django.utils.translation import gettext_lazy as _
from allauth.account.forms import SignupForm
from .models import Anuncio


class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        exclude = ("conductor",)
        widgets = {
            "hora_salida": forms.TimeInput(attrs={"type": "time"}),
            "hora_llegada": forms.TimeInput(attrs={"type": "time"}),
            "numero_contacto": forms.TextInput(attrs={"type": "tel"}),
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

