from django import forms

class CompetenciaFormulario(forms.Form):

  competencia = forms.CharField()
  camada = forms.IntegerField()