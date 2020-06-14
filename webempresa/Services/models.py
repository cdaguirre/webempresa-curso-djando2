from django.db import models

# Create your models here.

#python manage.py makemigrations portfolio este es para crear o actualizar los modelos
#python manage.py migrate portfolio este crea la app o lo tira a la app

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title