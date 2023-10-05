from django.db import models

# Create your models here.
class project (models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    link = models.URLField(null=True, blank=True, verbose_name="Direccion web")

# clase para que se vea el nombre en el admin
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyecto"
        ordering = ["-created"]
     


# para que se vea el titulo en el admin

    def __str__(self):
        return self.title