# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)


class NameForm(forms.Form):
    my_default_errors = {
        'required': 'Campo requerido',
        'invalid': 'Valores inválidos'
    }
    name = forms.CharField(label='Nombre', max_length=100, error_messages=my_default_errors)
    last_names = forms.CharField(label='Apellidos', max_length=100, error_messages=my_default_errors)
    email = forms.CharField(label='Correo', max_length=100, error_messages=my_default_errors, widget=forms.EmailInput)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Agregar', 'Agregar', css_class='btn-primary'))


class EditForm(forms.Form):
    my_default_errors = {
        'required': 'Campo requerido',
        'invalid': 'Valores inválidos'
    }
    editName = forms.CharField(label='Nombre', max_length=100, error_messages=my_default_errors)
    editLast_names = forms.CharField(label='Apellidos', max_length=100, error_messages=my_default_errors)
    editEmail = forms.CharField(label='Correo', max_length=100, error_messages=my_default_errors, widget=forms.EmailInput)
    editId = forms.CharField(required=True, label='')

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_action = '/usuarios/editar/'
    helper.add_input(Submit('Editar', 'Editar', css_class='btn-primary'))
