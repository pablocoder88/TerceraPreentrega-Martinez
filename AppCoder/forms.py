from django import forms

class CompetenciaFormulario(forms.Form):

  competencia = forms.CharField()
  camada = forms.IntegerField()
  
  
class NadadorFormulario(forms.Form):

  nadador = forms.CharField()
  
  
  
class EntrenadorFormulario(forms.Form):

  entrenador = forms.CharField()
  club = forms.CharField()