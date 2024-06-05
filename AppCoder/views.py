from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
def competencia(req, nombre, camada):

  nueva_competencia = Competencia(nombre=nombre, camada=camada)
  nueva_competencia.save()

  return HttpResponse(f"""
    <p>Competencia: {nueva_competencia.nombre} - Camada: {nueva_competencia.camada} creado!</p>
  """)

def lista_competencias(req):

  lista = Competencia.objects.all()

  return render(req, "lista_competencias.html", {"lista_competencias": lista})

def inicio(req):

  return render(req, "inicio.html", {})

def competencias(req):

  return render(req, "competencias.html", {})

def entrenadores(req):

  return render(req, "entrenadores.html", {})

def nadadores(req):

  return render(req, "nadadores.html", {})

def competencia_formulario(req):

  print('method: ', req.method)
  print('POST: ', req.POST)

  if req.method == 'POST':

    miFormulario = CompetenciaFormulario(req.POST)

    if miFormulario.is_valid():

      data = miFormulario.cleaned_data

      nueva_competencia = Competencia(nombre=data['competencia'], camada=data['camada'])
      nueva_competencia.save()

      return render(req, "inicio.html", {"message": "Competencia creada con éxito"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:

    miFormulario = CompetenciaFormulario()

    return render(req, "competencia_formulario.html", {"miFormulario": miFormulario})


def busqueda_camada(req):

    return render(req, "busqueda_camada.html", {})

def buscar(req):

  if req.GET["camada"]:

    camada = req.GET["camada"]

    competencias = Competencia.objects.filter(camada__icontains=camada)

    return render(req, "resultadoBusqueda.html", {"competencias": competencias, "camada": camada})

  else:
      
      return render(req, "inicio.html", {"message": "No envias el dato de la camada"})
    
    
def nadador_formulario(req):

  print('method: ', req.method)
  print('POST: ', req.POST)

  if req.method == 'POST':

    miFormularioN = NadadorFormulario(req.POST)

    if miFormularioN.is_valid():

      data = miFormularioN.cleaned_data

      nuevo_nadador = Nadador(nombre=data['nadador'])
      nuevo_nadador.save()

      return render(req, "inicio.html", {"message": "Nadador creado con éxito"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:

    miFormularioN = NadadorFormulario()

    return render(req, "nadador_formulario.html", {"miFormularioN": miFormularioN})


def entrenador_formulario(req):
  
  
  print('method: ', req.method)
  print('POST: ', req.POST)

  if req.method == 'POST':

    miFormularioE = EntrenadorFormulario(req.POST)

    if miFormularioE.is_valid():

      data = miFormularioE.cleaned_data

      nuevo_entrenador = Entrenador(nombre=data['entrenador'], club=data['club'])
      nuevo_entrenador.save()

      return render(req, "inicio.html", {"message": "Entrenador creado con éxito"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:

    miFormularioE = EntrenadorFormulario()

    return render(req, "entrenador_formulario.html", {"miFormularioE": miFormularioE})
