# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)
from usuarios.models import Usersys


class AddId(forms.Form):
    my_default_errors = {
        'required': 'Campo requerido',
        'invalid': 'Valores inválidos'
    }

    Usuario = forms.ModelChoiceField(required=True, queryset=Usersys.objects.all())
    # Tipo = forms.ModelChoiceField(required=True, queryset=Type.objects.all())
    String = forms.CharField(required=True, label='Cadena de identificacion')

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_action = '/identificacion/nuevo/'
    helper.add_input(Submit('Agregar', 'Agregar', css_class='btn-primary'))
