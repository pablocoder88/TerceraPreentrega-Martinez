from django import forms

class CompetenciaFormulario(forms.Form):

  evento = forms.CharField()
  record = forms.CharField()
  
  
class NadadorFormulario(forms.Form):

  nombre = forms.CharField()
  apellido = forms.CharField()
  


  
  
class EntrenadorFormulario(forms.Form):

  nombre = forms.CharField()
  apellido = forms.CharField()
  club = forms.CharField()
