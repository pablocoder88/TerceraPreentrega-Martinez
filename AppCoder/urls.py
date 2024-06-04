from django.urls import path
from AppCoder.views import (
  competencia, 
  lista_competencias, 
  inicio, 
  competencias, 
  entrenadores, 
  nadadores, 
  competencia_formulario,
  busqueda_camada,
  buscar
)

urlpatterns = [
    path('agrega-competencia/<nombre>/<camada>', competencia),
    path('lista-competencias/', lista_competencias),
    path('', inicio, name='Inicio'),
    path('competencias/', competencias, name='Competencias'),
    path('entrenadores/', entrenadores, name='Entrenadores'),
    path('nadadores/', nadadores, name='Nadadores'),
    path('competencia-formulario/', competencia_formulario, name='CompetenciaFormulario'),
    path('busqueda-camada/', busqueda_camada, name='BusquedaCamada'),
    path('buscar/', buscar, name='BuscarCompetencia'),
]
