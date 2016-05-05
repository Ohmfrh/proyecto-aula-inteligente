from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

from .models import Song
from multimedia.models import Server


class AddSong(forms.Form):
    Name = forms.CharField(required=True, label='Nombre del archivo')
    ServerList = forms.ModelChoiceField(required=True, queryset=Server.objects.all())
    Path = forms.CharField(required=True, label='Path')
    Artist = forms.CharField(required=True, label='Artist')
    Album = forms.CharField(required=True, label='Album')
    Image = forms.CharField(required=True, label='Image')

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_action = '/musica/agregar/'
    helper.add_input(Submit('Agregar', 'Agregar', css_class='btn-primary'))


class SongForm(forms.Form):
    Canciones = forms.ModelMultipleChoiceField(queryset=Song.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    UserOwner = forms.CharField(required=True, label='')

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_action = '/musica/usuario/'
    helper.add_input(Submit('Agregar', 'Agregar', css_class='btn-primary'))
    helper.layout = Layout(
        Field('Canciones', css_class="checkbox-inline"),
        Field('UserOwner', css_class="checkbox-inline", type="hidden"),
    )
    helper.html5_required = False


class EditSong(forms.Form):
    editName = forms.CharField(required=True, label='Nombre del archivo')
    editServerList = forms.ModelChoiceField(required=True, queryset=Server.objects.all())
    editPath = forms.CharField(required=True, label='Path')
    editArtist = forms.CharField(required=True, label='Artist')
    editAlbum = forms.CharField(required=True, label='Album')
    editImage = forms.CharField(required=True, label='Image')
    editId = forms.CharField(required=True, label='')

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_action = '/musica/editar/'
    helper.add_input(Submit('Agregar', 'Agregar', css_class='btn-primary'))