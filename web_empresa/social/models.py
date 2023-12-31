from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name= "Nombre clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Red social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(verbose_name="Creado", auto_now_add=True)
    updated = models.DateField(verbose_name="Actualizado", auto_now=True)
    class Meta():
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        ordering = ['-name']


    def __str__(self):
        return self.name       
