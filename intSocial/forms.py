from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class CrearNuevoUsuario(forms.Form):
    """
    FUERA DE USO
    """
    nombre = forms.CharField(label='Nombre', max_length=50)
    apellidos = forms.CharField(label='Apellidos', max_length=50)
    username = forms.CharField(label='Nombre de Usuario', max_length=50)
    email = forms.CharField(label='Correo Elctronico', max_length=255)
    contasenia = forms.CharField(label='Contraseña', max_length=60)


class CreateNewPost(forms.Form):
    """
    Permite crear una publicacion nueva
    """
    titulo = forms.CharField(label="Titulo", max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    contenido = forms.CharField(label="Detalles", widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    imagen = forms.ImageField(label='Imagen', allow_empty_file=True, required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))


class CreateNewComment(forms.Form):
    """
    Permite publicar un comentario
    """
    contenido = forms.CharField(label="Escribe tu comentario", widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

class UpdateUserForm(UserChangeForm):
    """
    Hace uso del Form de django para cambiar opciones del usuario
    """
    class Meta:
        model = User
        fields = ('username', 'email','first_name', 'last_name')