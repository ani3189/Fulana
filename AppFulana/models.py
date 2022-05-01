from django.db import models

# Create your models here.

class Posteos(models.Model):
    titulo = models.CharField(max_length=30)
    post = models.TextField()
    class Meta:
        verbose_name = "posteo"
        verbose_name_plural = "posteos"
    def __str__(self):
        txt = "{0}"
        return txt.format(self.titulo)

class Lenguaje(models.Model):
    lenguaje = models.CharField(max_length=30)
    review = models.TextField()
    class Meta:
        verbose_name = "lenguaje"
        verbose_name_plural = "lenguajes"
    def __str__(self):
        txt = "{0}"
        return txt.format(self.lenguaje)

class Institutos(models.Model):
    instituto = models.CharField(max_length=30)
    review = models.TextField()
    class Meta:
        verbose_name = "instituto"
        verbose_name_plural = "institutos"
    def __str__(self):
        txt = "{0}"
        return txt.format(self.instituto)
