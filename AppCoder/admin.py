from django.contrib import admin
from .models import Competencia, Entrenador, Nadador

class CompetenciaAdmin(admin.ModelAdmin):
  list_display = ['evento', 'record']
  search_fields = ['evento', 'record']
  list_filter = ['evento']

# Register your models here.
admin.site.register(Competencia, CompetenciaAdmin)
admin.site.register(Entrenador)
admin.site.register(Nadador)


