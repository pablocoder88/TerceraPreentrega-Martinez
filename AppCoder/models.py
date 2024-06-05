from django.db import models

# Create your models here.
class Competencia(models.Model):

  nombre = models.CharField(max_length=40)
  camada = models.IntegerField()

  def __str__(self):
    return f'{self.nombre} - {self.camada}'
  
  class Meta():

    verbose_name = 'Competence'
    verbose_name_plural = 'Competences'
    ordering = ('nombre', 'camada')
    unique_together = ('nombre', 'camada')

class Nadador(models.Model):

  nombre = models.CharField(max_length=30)
  apellido = models.CharField(max_length=30)
  email = models.EmailField(null=True)
  competencias = models.ManyToManyField(Competencia)

  def __str__(self):
    return f'{self.nombre} - {self.apellido}'

class Entrenador(models.Model):

  nombre = models.CharField(max_length=30)
  apellido = models.CharField(max_length=30)
  email = models.EmailField()
  club = models.CharField(max_length=30)
