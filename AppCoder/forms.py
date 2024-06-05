from django import forms

class CompetenciaFormulario(forms.Form):

  evento = forms.CharField()
  record = forms.CharField()
  
  
class NadadorFormulario(forms.Form):

  nadador = forms.CharField()
  
  
  
class EntrenadorFormulario(forms.Form):

  entrenador = forms.CharField()
  club = forms.CharField()