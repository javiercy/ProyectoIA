from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuario(models.Model):
    """
    Datos necesarios de un usuario, NO USADO,
    CAMBIADO POR EL DE DEFECTO DE DJANGO, SIN EMBARGO, 
    USAN CASI LOS MISMOS DATOS, TOAR EN CUENTA PARA EL MODELO
    """
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=255, unique=True)
    contasenia = models.CharField(max_length=60)
    esta_Activo = models.BooleanField(default=True)
    es_Admin = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Level(models.Model):
    """
    Nivel de privaciodad, TECNICAMENTE SE USA, 
    PERO A LA VEZ NO (DENTRO DE LA LOGICA (SOLO EXISTE PUBLICO))
    """
    name = models.CharField(max_length=50)  # 1 publico, 2 privado, 3 grupo


class Profile(models.Model):
    """
    Datos extras que tiene un usuario y que puede personalizar con libertad
    """
    fecha_nacimiento = models.DateField(null=True)
    genero = models.CharField(max_length=10, null=True)
    imagen = models.ImageField(null=True, blank=True, upload_to="images/")
    imagen_header = models.ImageField(null=True, blank=True, upload_to="images/")
    titulo = models.CharField(max_length=255, null=True)
    bio = models.CharField(max_length=255, null=True)
    info_contacto = models.TextField(null=True)
    email_publico = models.CharField(max_length=255, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, default=1)

    # def __str__(self):
    #     return self.usuario.username + ' ' + self.titulo


class Portafolio(models.Model):
    """
    También se les podrian considerar albums, NO SE USA
    """
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username + ' ' + self.titulo


class Imagen(models.Model):
    """
    Datos para almacenar y hacer refencias a imagenes
    """
    src = models.ImageField(null=True, blank=True, upload_to="images/")
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    portafolio = models.ForeignKey(Portafolio, on_delete=models.SET_NULL, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username + ' ' + self.titulo


class Post(models.Model):
    """
    Post o publicaciones
    """
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)
    receptor_type = models.IntegerField()
    categoria = models.CharField(max_length=50,null=True)
    post_type = models.IntegerField(default=1)

    def __str__(self):
        return self.autor.username + ' ' + self.titulo


class PostImagen(models.Model):
    """Muchos a muchos (Post-Imagen)"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    imagen = models.ForeignKey(Imagen, on_delete=models.CASCADE)


class Likes(models.Model):
    """
    Likes y dislikes
    """
    valor = models.IntegerField()  # 1 like, 2 dislike
    ref = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username + ' ' + self.creado_en


class Comentario(models.Model):
    """
    Para hacer comentarios
    """
    ref = models.ForeignKey(Post, on_delete=models.CASCADE)  # post en el que se encuentra
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    respuesta_a = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='respuestas')
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' a ' + self.ref.autor.username


class Notificaciones(models.Model):
    """
    Permite guardar las notificaciones recibidas
    """
    not_type = models.IntegerField()  # 1 likes, 2 comentarios
    ref = models.ForeignKey(Post, on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notificaciones_recibe')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notificaciones_envia')
    fue_leido = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)


class Grupos(models.Model):
    """
    NO SE USA
    """
    imagen = models.CharField(max_length=255)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField()  # 1 open, 2 closed
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Encuesta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=20)
    genero_preferido = models.CharField(max_length=50)
    ocupacion = models.CharField(max_length=20)
    personalidad = models.CharField(max_length=20)
    paz_interior = models.CharField(max_length=20)
    sueño = models.CharField(max_length=50)
    tiempo_de_juego = models.CharField(max_length=20)
    horario = models.CharField(max_length=20)
    dias_de_juego = models.CharField(max_length=20)
    escuchas_musica_mientras_juegas = models.CharField(max_length=10)
    enfoque_de_juego = models.CharField(max_length=20)
    plataforma_preferida = models.CharField(max_length=20)
    comunicacion = models.CharField(max_length=20)
    modalidad_de_juego = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Encuesta de {self.user.username}" if self.user else "Encuesta anónima"

class Encuesta_peso(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        edad_peso = models.FloatField(default=0)  # Campo para almacenar el peso de la edad
        sexo_peso = models.FloatField(default=0)  # Campo para almacenar el peso del sexo
        genero_preferido_peso = models.FloatField(default=0)  # Campo para almacenar el peso del género preferido
        ocupacion_peso = models.FloatField(default=0)  # Campo para almacenar el peso de la ocupación
        personalidad_peso = models.FloatField(default=0)  # Campo para almacenar el peso de la personalidad
        paz_interior_peso = models.FloatField(default=0)  # Campo para almacenar el peso de la paz interior
        sueño_peso = models.FloatField(default=0)  # Campo para almacenar el peso de los hábitos de sueño
        tiempo_de_juego_peso = models.FloatField(default=0)  # Campo para almacenar el peso del tiempo de juego
        horario_peso = models.FloatField(default=0)  # Campo para almacenar el peso del horario de juego
        dias_de_juego_peso = models.FloatField(default=0)  # Campo para almacenar el peso de los días de juego
        escuchas_musica_mientras_juegas_peso = models.FloatField(default=0)  # Campo para almacenar el peso de escuchar música mientras juegas
        enfoque_de_juego_peso = models.FloatField(default=0)  # Campo para almacenar el peso del enfoque de juego
        plataforma_preferida_peso = models.FloatField(default=0)  # Campo para almacenar el peso de la plataforma preferida
        comunicacion_peso = models.FloatField(default=0)  # Campo para almacenar el peso de la comunicación
        modalidad_de_juego_peso = models.FloatField(default=0)  # Campo para almacenar el peso de la modalidad de juego
        total_pesos = models.FloatField(default=0)  # Campo para almacenar la suma total de los pesos
        creado_en = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"Encuesta de {self.user.username}" if self.user else "Encuesta anónima"

class Match(models.Model):
        usuario1 = models.ForeignKey(User, related_name='match_usuario1', on_delete=models.CASCADE)
        usuario2 = models.ForeignKey(User, related_name='match_usuario2', on_delete=models.CASCADE)
        fecha_match = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f'Match entre {self.usuario1.username} y {self.usuario2.username}'