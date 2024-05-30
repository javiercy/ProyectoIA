from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Encuesta_peso

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





class CreateNewForm(forms.ModelForm):
    # Definición de opciones de campos
    edad_choices = [('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26')]
    sexo_choices = [('Femenino', 'Femenino'), ('Masculino', 'Masculino'), ('No proporcionado', 'No proporcionado')]
    genero_preferido_choices = [('Aventura', 'Aventura'), ('Acción', 'Acción'), ('Rol', 'Rol'), ('FPS', 'FPS'), ('Estrategia', 'Estrategia'), ('Peleas', 'Peleas'), ('Simulación', 'Simulación'), ('Mundo abierto', 'Mundo abierto'), ('Carreras', 'Carreras')]
    ocupacion_choices = [('Estudiante', 'Estudiante'), ('Trabajador', 'Trabajador'), ('Becario', 'Becario')]
    personalidad_choices = [('Introvertid(o/a)', 'Introvertid(o/a)'), ('Ambivertid(o/a)', 'Ambivertid(o/a)'), ('Extrovertid(o/a)', 'Extrovertid(o/a)'), ('Sin especificar', 'Sin especificar')]
    paz_interior_choices = [('Tranquilo', 'Tranquilo'), ('Reactivo', 'Reactivo'), ('Nervioso', 'Nervioso'), ('Alegre', 'Alegre'), ('Indiferente', 'Indiferente'), ('Euforico', 'Euforico')]
    sueño_choices = [('Regulares (dormir de noche)', 'Regulares (dormir de noche)'), ('Invertidos (vivir de noche)', 'Invertidos (vivir de noche)'), ('Irregulares', 'Irregulares')]
    tiempo_de_juego_choices = [('0-1 horas', '0-1 horas'), ('1-2 horas', '1-2 horas'), ('2-3 horas', '2-3 horas'), ('3-4 horas', '3-4 horas'), ('4-5 horas', '4-5 horas'), ('5 o más', '5 o más')]
    horario_choices = [('Mañana', 'Mañana'), ('Día', 'Día'), ('Tarde-noche', 'Tarde-noche'), ('Madrugada', 'Madrugada')]
    dias_de_juego_choices = [('Entre semana', 'Entre semana'), ('Fines de semana', 'Fines de semana'), ('Toda la semana', 'Toda la semana')]
    escuchas_musica_mientras_juegas_choices = [('Sí', 'Sí'), ('No', 'No'), ('Da igual', 'Da igual')]
    enfoque_de_juego_choices = [('Competitivo', 'Competitivo'), ('Casual', 'Casual')]
    plataforma_preferida_choices = [('Xbox', 'Xbox'), ('Playstation', 'Playstation'), ('Nintendo', 'Nintendo'), ('PC', 'PC'), ('Móvil', 'Móvil')]
    comunicacion_choices = [('Mic in game', 'Mic in game'), ('Chat de texto', 'Chat de texto'), ('Llamada a parte', 'Llamada a parte'), ('Da igual', 'Da igual')]
    modalidad_de_juego_choices = [('En persona', 'En persona'), ('En linea', 'En linea'), ('Da igual', 'Da igual')]

    # Definición de campos  
    edad = forms.ChoiceField(choices=edad_choices)
    sexo = forms.ChoiceField(choices=sexo_choices)
    genero_preferido = forms.ChoiceField(choices=genero_preferido_choices)
    ocupacion = forms.ChoiceField(choices=ocupacion_choices)
    personalidad = forms.ChoiceField(choices=personalidad_choices)
    paz_interior = forms.ChoiceField(choices=paz_interior_choices)
    sueño = forms.ChoiceField(choices=sueño_choices)
    tiempo_de_juego = forms.ChoiceField(choices=tiempo_de_juego_choices)
    horario = forms.ChoiceField(choices=horario_choices)
    dias_de_juego = forms.ChoiceField(choices=dias_de_juego_choices)
    escuchas_musica_mientras_juegas = forms.ChoiceField(choices=escuchas_musica_mientras_juegas_choices)
    enfoque_de_juego = forms.ChoiceField(choices=enfoque_de_juego_choices)
    plataforma_preferida = forms.ChoiceField(choices=plataforma_preferida_choices)
    comunicacion = forms.ChoiceField(choices=comunicacion_choices)
    modalidad_de_juego = forms.ChoiceField(choices=modalidad_de_juego_choices)

    class Meta:
        model = Encuesta_peso
        fields = ['edad', 'sexo', 'genero_preferido', 'ocupacion', 'personalidad', 'paz_interior', 'sueño', 'tiempo_de_juego', 'horario', 'dias_de_juego', 'escuchas_musica_mientras_juegas', 'enfoque_de_juego', 'plataforma_preferida', 'comunicacion', 'modalidad_de_juego']
        exclude = ['user', 'total_pesos']       

    def save(self, user, commit=True):
        instance = super().save(commit=False)
        instance.user = user

        # Calcula los pesos individuales
        instance.edad_peso = self.calcular_peso('edad')
        instance.sexo_peso = self.calcular_peso('sexo')
        instance.genero_preferido_peso = self.calcular_peso('genero_preferido')
        instance.ocupacion_peso = self.calcular_peso('ocupacion')
        instance.personalidad_peso = self.calcular_peso('personalidad')
        instance.paz_interior_peso = self.calcular_peso('paz_interior')
        instance.sueño_peso = self.calcular_peso('sueño')
        instance.tiempo_de_juego_peso = self.calcular_peso('tiempo_de_juego')
        instance.horario_peso = self.calcular_peso('horario')
        instance.dias_de_juego_peso = self.calcular_peso('dias_de_juego')
        instance.escuchas_musica_mientras_juegas_peso = self.calcular_peso('escuchas_musica_mientras_juegas')
        instance.enfoque_de_juego_peso = self.calcular_peso('enfoque_de_juego')
        instance.plataforma_preferida_peso = self.calcular_peso('plataforma_preferida')
        instance.comunicacion_peso = self.calcular_peso('comunicacion')
        instance.modalidad_de_juego_peso = self.calcular_peso('modalidad_de_juego')

        # Calcula el peso total
        instance.total_pesos = sum([
        instance.edad_peso, instance.sexo_peso, instance.genero_preferido_peso,
        instance.ocupacion_peso, instance.personalidad_peso, instance.paz_interior_peso,
        instance.sueño_peso,instance.tiempo_de_juego_peso,instance.horario_peso, instance.dias_de_juego_peso, instance.escuchas_musica_mientras_juegas_peso,
        instance.enfoque_de_juego_peso, instance.plataforma_preferida_peso,
        instance.comunicacion_peso, instance.modalidad_de_juego_peso
        ])

        if commit:
            instance.save()
        return instance

    def calcular_peso(self, field):
        cleaned_data = self.cleaned_data
        if not cleaned_data:
            return 0
        
        value = cleaned_data.get(field)
        pesos = {
            'edad': {'18': 0.1, '19': 0.2, '20': 0.3, '21': 0.4, '22': 0.5, '23': 0.6, '24': 0.7, '25': 0.8, '26': 0.9},
            'sexo': {'Femenino': 0.1, 'Masculino': 0.2, 'No proporcionado': 0.3},
            'genero_preferido': {'Aventura': 0.1, 'Acción': 0.2, 'Rol': 0.3, 'FPS': 0.4, 'Estrategia': 0.5,
                                'Peleas': 0.6, 'Simulación': 0.7, 'Mundo abierto': 0.8, 'Carreras': 0.9},
            'ocupacion': {'Estudiante': 0.1, 'Trabajador': 0.2, 'Becario': 0.3},
            'personalidad': {'Introvertid(o/a)': 0.1, 'Ambivertid(o/a)': 0.2, 'Extrovertid(o/a)': 0.3,
                            'Sin especificar': 0.4},
            'paz_interior': {'Tranquilo': 0.1, 'Reactivo': 0.2, 'Nervioso': 0.3, 'Alegre': 0.4, 'Indiferente': 0.5, 'Euforico': 0.6},
            'sueño': {'Regulares (dormir de noche)': 0.1, 'Invertidos (vivir de noche)': 0.2, 'Irregulares': 0.3},
            'tiempo_de_juego': {'0-1 horas': 0.1, '1-2 horas': 0.2, '2-3 horas': 0.3, '3-4 horas': 0.4, '4-5 horas': 0.5, '5 o más': 0.6},
            'horario': {'Mañana': 0.1, 'Día': 0.2, 'Tarde-noche': 0.3, 'Madrugada': 0.4},
            'dias_de_juego': {'Entre semana': 0.1, 'Fines de semana': 0.2, 'Toda la semana': 0.3},
            'escuchas_musica_mientras_juegas': {'Sí': 0.1, 'No': 0.2, 'Da igual': 0.3},
            'enfoque_de_juego': {'Competitivo': 0.1, 'Casual': 0.2},
            'plataforma_preferida': {'Xbox': 0.1, 'Playstation': 0.2, 'Nintendo': 0.3, 'PC': 0.4, 'Móvil': 0.5},
            'comunicacion': {'Mic in game': 0.1, 'Chat de texto': 0.2, 'Llamada a parte': 0.3, 'Da igual': 0.4},
            'modalidad_de_juego': {'En persona': 0.1, 'En linea': 0.2, 'Da igual': 0.3}
        }

        return pesos.get(field, {}).get(value, 0)
