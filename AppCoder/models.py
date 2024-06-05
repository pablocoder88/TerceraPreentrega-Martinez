from django.db import models

# Create your models here.
class Competencia(models.Model):

  evento = models.CharField(max_length=40)
  record = models.CharField(max_length=40, null=True)

  def __str__(self):
    return f'{self.evento} - {self.record}'
  
  class Meta():

    verbose_name = 'Competencia'
    verbose_name_plural = 'Competencias'


class Nadador(models.Model):

  nombre = models.CharField(max_length=30)
  apellido = models.CharField(max_length=30)
  email = models.EmailField(null=True)
  competencias = models.ManyToManyField(Competencia)
  
  class Meta():

    verbose_name = 'Nadador'
    verbose_name_plural = 'Nadadores'


  def __str__(self):
    return f'{self.nombre} - {self.apellido}'

class Entrenador(models.Model):

  nombre = models.CharField(max_length=30)
  apellido = models.CharField(max_length=30)
  email = models.EmailField()
  club = models.CharField(max_length=30)
  
  class Meta():
    verbose_name = 'Entrenador'
    verbose_name_plural = 'Entrenadores'
    
  def __str__(self):
    return f'{self.nombre} - {self.apellido} - {self.club}'    



  
