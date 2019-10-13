from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombres = models.CharField(max_length=50, blank=False)
    apellidos = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=20, blank=False)
    url_foto = models.CharField(max_length=255, blank=False, null=False)
    perfil_prof = models.CharField(max_length=1000, blank=False)


class Portafolio(models.Model):
    titulo = models.CharField(max_length=80, blank=False)
    url_imag = models.CharField(max_length=255, blank=False, null=False)
    descripcion = models.CharField(max_length=200)
    tipo_archivo = models.CharField(max_length=10)
    is_private = models.BooleanField()
    owner = models.ForeignKey(
        Usuario, blank=False, null=False, on_delete=models.CASCADE)

