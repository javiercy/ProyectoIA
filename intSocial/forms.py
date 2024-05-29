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
    categorias = [
        ('Off-topic','Off-topic'),
        ('Food', 'Food'),
        ('Cars', 'Cars'),
        ('Beauty','Beauty'),
        ('Sports','Sports'),
        ('Electronics','Electronics'),
        ('Handmade','Handmade'),
        ('Housewares','Housewares'),
        ('Music','Music'),
        ('Toys','Toys'),
        ('Books','Books'),
        ('Pets','Pets'),
        ('Clothes','Clothes'),
        ('Videogames','Videogames'),
    ]
    categoria = forms.ChoiceField(
        choices=categorias,
        widget=forms.Select(attrs={'class':'form-control'})
    )


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
        fields = ('username', 'email')

        
class CreateNewSurvey(forms.Form):
    edad = forms.ChoiceField(
        choices=[(str(i), str(i)) for i in range(18, 27)],
        label="Edad",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    sexo = forms.ChoiceField(
        choices=[
            ('Femenino', 'Femenino'),
            ('Masculino', 'Masculino'),
            ('No proporcionado', 'No proporcionado')
        ],
        label="Sexo",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    genero_preferido = forms.ChoiceField(
        choices=[
            ('Aventura', 'Aventura'),
            ('Acción', 'Acción'),
            ('Rol', 'Rol'),
            ('FPS', 'FPS'),
            ('Estrategia', 'Estrategia'),
            ('Peleas', 'Peleas'),
            ('Simulación', 'Simulación'),
            ('Mundo abierto', 'Mundo abierto'),
            ('Carreras', 'Carreras')
        ],
        label="Género de juego preferido",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    ocupacion = forms.ChoiceField(
        choices=[
            ('Estudiante', 'Estudiante'),
            ('Trabajador', 'Trabajador'),
            ('Becario', 'Becario')
        ],
        label="Ocupación",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    personalidad = forms.ChoiceField(
        choices=[
            ('Introvertid(o/a)', 'Introvertid(o/a)'),
            ('Ambivertid(o/a)', 'Ambivertid(o/a)'),
            ('Extrovertid(o/a)', 'Extrovertid(o/a)'),
            ('Sin especificar', 'Sin especificar')
        ],
        label="Personalidad",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    paz_interior = forms.ChoiceField(
        choices=[
            ('Tranquilo', 'Tranquilo'),
            ('Reactivo', 'Reactivo'),
            ('Nervioso', 'Nervioso'),
            ('Alegre', 'Alegre'),
            ('Indiferente', 'Indiferente'),
            ('Euforico', 'Euforico')
        ],
        label="Paz interior",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    sueño = forms.ChoiceField(
        choices=[
            ('Regulares (dormir de noche)', 'Regulares (dormir de noche)'),
            ('Invertidos (vivir de noche)', 'Invertidos (vivir de noche)'),
            ('Irregulares', 'Irregulares')
        ],
        label="Hábitos de sueño",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    tiempo_de_juego = forms.ChoiceField(
        choices=[
            ('0-1 horas', '0-1 horas'),
            ('1-2 horas', '1-2 horas'),
            ('2-3 horas', '2-3 horas'),
            ('3-4 horas', '3-4 horas'),
            ('4-5 horas', '4-5 horas'),
            ('5 o más', '5 o más')
        ],
        label="Tiempo de juego",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    horario = forms.ChoiceField(
        choices=[
            ('Mañana', 'Mañana'),
            ('Día', 'Día'),
            ('Tarde-noche', 'Tarde-noche'),
            ('Madrugada', 'Madrugada')
        ],
        label="Horario de juego",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    dias_de_juego = forms.ChoiceField(
        choices=[
            ('Entre semana', 'Entre semana'),
            ('Fines de semana', 'Fines de semana'),
            ('Toda la semana', 'Toda la semana')
        ],
        label="Días de juego",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    escuchas_musica_mientras_juegas = forms.ChoiceField(
        choices=[
            ('Sí', 'Sí'),
            ('No', 'No'),
            ('Da igual', 'Da igual')
        ],
        label="Escuchas música mientras juegas",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    enfoque_de_juego = forms.ChoiceField(
        choices=[
            ('Competitivo', 'Competitivo'),
            ('Casual', 'Casual')
        ],
        label="Enfoque de juego",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    plataforma_preferida = forms.ChoiceField(
        choices=[
            ('Xbox', 'Xbox'),
            ('Playstation', 'Playstation'),
            ('Nintendo', 'Nintendo'),
            ('PC', 'PC'),
            ('Móvil', 'Móvil')
        ],
        label="Plataforma preferida",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    comunicacion = forms.ChoiceField(
        choices=[
            ('Mic in game', 'Mic in game'),
            ('Chat de texto', 'Chat de texto'),
            ('Llamada a parte', 'Llamada a parte'),
            ('Da igual', 'Da igual')
        ],
        label="Comunicación",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    modalidad_de_juego = forms.ChoiceField(
        choices=[
            ('En persona', 'En persona'),
            ('En linea', 'En linea'),
            ('Da igual', 'Da igual')
        ],
        label="Modalidad de juego",
        widget=forms.Select(attrs={'class': 'form-control'})
    )