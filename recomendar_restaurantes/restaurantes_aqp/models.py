from django.db import models
from django.contrib.auth.models import User

class CategoriaRestaurante(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_cocina = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    categoria = models.ForeignKey(CategoriaRestaurante, on_delete=models.CASCADE)
    capacidad = models.PositiveSmallIntegerField(default=0) 
    horario_apertura = models.TimeField(default='00:00')  
    horario_cierre = models.TimeField(default='23:59') 
    tiene_entrega_domicilio = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    restaurante = models.ForeignKey('Restaurante', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f"Calificación de {self.valor} para {self.restaurante.nombre} por {self.usuario.username}"

class Comentario(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.restaurante.nombre}"