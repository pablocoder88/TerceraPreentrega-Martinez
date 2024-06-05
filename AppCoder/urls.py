from django.urls import path
from AppCoder.views import (
  competencia, 
  lista_competencias, 
  inicio, 
  competencias, 
  entrenadores, 
  nadadores, 
  competencia_formulario,
  busqueda_evento,
  buscar,
  nadador_formulario,
  entrenador_formulario
)

urlpatterns = [
    path('agrega-competencia/<evento>/<record>', competencia),
    path('lista-competencias/', lista_competencias),
    path('', inicio, name='Inicio'),
    path('competencias/', competencias, name='Competencias'),
    path('entrenadores/', entrenadores, name='Entrenadores'),
    path('nadadores/', nadadores, name='Nadadores'),
    path('competencia-formulario/', competencia_formulario, name='CompetenciaFormulario'),
    path('busqueda-evento/', busqueda_evento, name='BusquedaEvento'),
    path('buscar/', buscar, name='BuscarCompetencia'),
    path('nadador-formulario/', nadador_formulario, name='NadadorFormulario'),
    path('entrenador-formulario/', entrenador_formulario, name='EntrenadorFormulario')
]
